<template>
  <!-- 此页面用来展示搜索结果 -->
  <div style="height: 100%">
    <el-container style="height: 100%">
      <el-header class="container hc_header">
        <el-row :gutter="20" style="z-index: 10">
          <el-col :span="4" style="margin-top: 10px">
            <span
              @click="returnIndexPage"
              style="float: left; font-size: 25px; font-weight: bold"
              >Paper Search
            </span>
          </el-col>

          <el-col :span="5" style="margin-top: 10px">
            <el-input
              id="searchInput"
              v-model="wd"
              @keyup.enter.native="submitWd"
            >
              <el-button slot="append" @click="submitWd_thispage"
                >搜一下</el-button
              >
            </el-input>
          </el-col>
          <el-col :span="8" :offset="3" class="hc_hotwd">
            <span style="color: black">热门搜索：</span>
            <span v-for="(hwd, index) in hotwd" :key="index">
              <a class="hot" href="#" :id="index" @click="submitHotWd(index)">{{
                hwd
              }}</a>
              &nbsp;&nbsp;
            </span>
          </el-col>
        </el-row>
      </el-header>
      <!-- 检索范围选择 -->
      <div
        style="
          clear: both;
          padding: 10px;
          margin-left: 20px;
          margin-right: 20px;
        "
      >
        <!-- <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="All" name="first">All</el-tab-pane>
          >
        </el-tabs> -->
      </div>
      <!-- 排序方式选项 -->
      <div>
        <div
          style="
            clear: both;
            padding: 10px;
            margin-left: 20px;
            margin-right: 200px;
          "
        >
          <span style="float: left"
            >About {{ this.total }} results ({{
              this.returntime
            }}
            seconds)</span
          >
          <el-select
            v-model="order"
            placeholder="排序方式"
            style="float: right"
          >
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </div>
      </div>
      <!-- 搜索结果展示 -->
      <el-container style="height = 100%;display: flex;">
        <el-main>
          <!-- 新的展示界面 -->
          <div style="overflow: hidden; clear: both">
            <!-- 题目 -->
            <div
              v-for="(result, index) in info"
              style="padding-top: 10px; padding-left: 20px"
            >
              <div style="max-width: 80%">
                <a
                  style="
                    text-align: left;
                    color: #2196f3;
                    max-width: 70%;
                    font-weight: bold;
                  "
                  @click="jump2info(result)"
                >
                  {{ result.title }}
                </a>
              </div>
              <div style="overflow: hidden; clear: both; height: 130px">
                <img
                  style="float: left; width: 7%"
                  src="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcR7oFivRR4gLzcfs8wi9WJv2v81KVBVQiABQEhGCdShjgjic5tC7D8NajEp"
                />
                <!-- 时间 作者 -->
                <p
                  style="
                    padding-top: 2px;

                    font-size: 10px;
                    margin-top: 5px;
                  "
                >
                  <span style="color: #ff5722">Publish Time:</span>

                  <span>{{ result.publish_at }}</span>
                  <span style="color: #009688">Author:</span>
                  <span v-for="(author, index) in result.author">{{
                    author
                  }}</span>
                </p>

                <!-- Publisher -->
                <p
                  v-if="result.publisher != ''"
                  style="padding-top: 2px;color：red;font-size: 10px;margin-top: 5px;"
                >
                  <span style="color: #ff5722">Publisher:</span>

                  <span>{{ result.publisher }}</span>
                </p>
                <!-- 摘要 -->
                <div
                  style="
                    max-width: 50%;
                    float: left;
                    width: 90%;
                    font: 13px/21px Arial, sans-serif;
                  "
                >
                  <p
                    style="
                      marigin: 10px;
                      max-height: 130px;
                      text-overflow: ellipsis;
                      -o-text-overflow: ellipsis;
                      overflow: hidden;
                    "
                  >
                    {{ result.abstract }}
                  </p>
                </div>
              </div>

              <!-- PDF -->
              <div style="font-weight: bold">
                <a
                  style="
                    text-align: left;
                    color: #673ab7;
                    font: 13px/21px Arial, sans-serif;
                    font-weight: bold;
                  "
                  v-bind:href="result.pdf"
                  v-if="result.pdf != ''"
                  >PDF</a
                >
                <a
                  style="
                    text-align: left;
                    color: #03a9f4;
                    font: 13px/21px Arial, sans-serif;
                    font-weight: bold;
                  "
                  v-bind:href="result.video"
                  v-if="result.video.search('39.96.43.48') != -1"
                  >Local Video</a
                >
                <a
                  style="
                    text-align: left;
                    color: #e91e63;
                    font: 13px/21px Arial, sans-serif;
                    font-weight: bold;
                  "
                  v-bind:href="result.video"
                  v-if="
                    result.video != '' &&
                    result.video.search('39.96.43.48') === -1
                  "
                  >Stream Video</a
                >
                <a
                  style="
                    text-align: left;
                    color: #f44336;
                    font: 13px/21px Arial, sans-serif;
                    font-weight: bold;
                  "
                  v-bind:href="result.dataset_url"
                  v-if="result.dataset_url != ''"
                  >Dataset</a
                >
              </div>
            </div>
          </div>
        </el-main>
      </el-container>

      <!--    下方的页码导航条 page-size规定每页的结果个数 page-count为总共的页数-->
      <div class="block hc_page" v-if="showPage">
        <el-pagination
          background
          :page-size="pageSize"
          :page-count="pageCount"
          :current-page.sync="currentPage"
          layout="prev, pager, next"
          @current-change="judge"
        >
        </el-pagination>
      </div>

      <el-footer class="hc_footer">
        <span>不得非法使用 :免责声明</span><br />
        <span>@2021 Website-HelloWorld</span>
      </el-footer>
    </el-container>
    <div
      v-loading="loading"
      :style="loadingBox"
      v-if="loading == true ? true : false"
    ></div>
  </div>
</template>

<script>
import AdvancedSearchVue from "./AdvancedSearch.vue";
export default {
  name: "SearchPage",

  data() {
    return {
      hotwd: ["1", "2", "3", "4", "5", "6"],
      wd: this.$route.query.keyword, //传来的keyword
      theme: this.$route.query.theme, //传来的theme
      options: [
        {
          value: "",
          label: "相关度",
        },
        {
          value: 1,
          label: "时间正序",
        },
        {
          value: 2,
          label: "时间逆序",
        },
      ],
      order: "", //排序0 1 2，
      year: "", //检索年份 多个用，隔开
      pagefrom: "", //来自哪个页面 1普通搜索 2高级搜索
      form: this.$route.query.form,
      getWd: "",
      total: "",
      returntime: "",
      pageSize: 10,
      pageCount: 100,
      currentPage: 0,
      showPage: false,
      info: [],
      loading: false,
      loadingBox: {
        position: "fixed",
        top: "65px",
        width: "100%",
        height: "",
      },
      // flag:true // 判定是否是初次加载
    };
  },
  watch: {
    order: function (val, oldVal) {
      // console.log(val);
      if (this.pagefrom === "1") {
        this.submitWd();
      } else {
        this.advancedSearch(this.form);
      }
    },
  },
  created() {
    this.getHeight();
  },
  mounted: function () {
    // 页面加载时需要触发的函数
    this.judge();
  },
  methods: {
    judge() {
      if (this.$route.query.keyword != undefined) {
        console.log("跳转来自：普通检索");
        this.pagefrom = "1";
        this.submitWd();
      } else {
        // console.log("跳转来自：高级检索");
        this.pagefrom = "2";
        this.advancedSearch(this.form);
      }
    },
    getHeight() {
      this.loadingBox.height = window.innerHeight - 65 + "px";
    },
    jump2info(thispageparams) {
      this.$router.push({
        path: "/pageinfo",
        query: { Infos: thispageparams },
      });
    },
    returnIndexPage() {
      this.$router.push({ path: "/" });
    },
    submitWd_thispage() {
      //此界面为普通搜索 把其他条件都清空
      this.year = "";
      this.theme = "";
      this.submitWd();
    },
    advancedSearch(form) {
      //高级检索
      var query = {
        author: form.author,
        logic: form.status,
        title: form.title,
      };
      this.wd = query;
      this.year = form.date;
      this.loading = true;
      this.page = 0;
      let date1 = new Date();
      let second1 = date1.getSeconds();
      let millisecond1 = date1.getMilliseconds();
      this.axios
        .get(
          "http://39.96.43.48/search?query=" +
            query +
            "&page=" +
            this.currentPage +
            "&order=" +
            this.order +
            "&year=" +
            this.year
        )
        .then((response) => {
          // alert("ok");
          console.log(response.data);
          //计算页数
          this.total = response.data.total;
          if (response.total % 10 != 0) {
            this.pageCount = Math.floor(response.data.total / 10) + 1;
            this.showPage = true;
          } else {
            this.pageCount = response.data.total / 10;
            this.showPage = true;
          }
          // this.info = JSON.parse(response.data);
          this.info = response.data.data;
          this.loading = false;
          //计算检索时间
          let date2 = new Date();
          let second2 = date2.getSeconds();
          let millisecond2 = date2.getMilliseconds();
          console.log(second1);
          //检索时间
          if (second2 - second1 > 0) {
            this.returntime = second2 - second1;
          } else if (second2 === second1) {
            if (millisecond2 - millisecond1 > 0) {
              this.returntime = (millisecond2 - millisecond1) / 1000;
            } else {
              this.returntime = (1000 + millisecond2 - millisecond1) / 1000;
            }
          }
        })
        .catch((err) => {
          // alert("error");
          console.log(err);
          this.info = [];
          this.showPage = false;
          this.loading = false;
        })
        .finally(() => {});
    },
    //后台请求数据
    submitWd() {
      this.goTop();
      // 如果检索词为空
      if (this.wd == "") {
        this.info = [];
        this.getWd = "";
        this.showPage = false;
      } else {
        this.loading = true;
        this.getWd = this.wd;
        this.page = 0;
        let date1 = new Date();
        let second1 = date1.getSeconds();
        let millisecond1 = date1.getMilliseconds();
        this.axios
          .get(
            "http://39.96.43.48/search?query=" +
              this.getWd +
              "&theme=" +
              this.theme +
              "&page=" +
              this.currentPage +
              "&order=" +
              this.order +
              "&year=" +
              this.year
          )
          .then((response) => {
            // alert("ok");
            console.log(response);
            this.total = response.data.total;
            if (response.total % 10 != 0) {
              this.pageCount = Math.floor(response.data.total / 10) + 1;
              this.showPage = true;
            } else {
              this.pageCount = response.data.total / 10;
              this.showPage = true;
            }
            // this.info = JSON.parse(response.data);
            this.info = response.data.data;
            this.loading = false;

            let date2 = new Date();
            let second2 = date2.getSeconds();
            let millisecond2 = date2.getMilliseconds();
            console.log(second1);
            console.log;
            //检索时间
            if (second2 - second1 > 0) {
              this.returntime = second2 - second1;
            } else if (second2 === second1) {
              if (millisecond2 - millisecond1 > 0) {
                this.returntime = (millisecond2 - millisecond1) / 1000;
              } else {
                this.returntime = (1000 + millisecond2 - millisecond1) / 1000;
              }
            }
          })
          .catch((err) => {
            // alert("error");
            console.log(err);
            this.info = [];
            this.showPage = false;
            this.loading = false;
          })
          .finally(() => {});
      }
    },
    //请求第val页的结果 接口接收keyword+val 返回page-size个第val页的检索结果
    submitPage(val) {
      if (this.wd == "") {
        if (this.getWd != "") {
          this.wd = this.getWd;
          this.submitRealForPage(val);
        } else {
          this.info = [];
        }
      } else {
        this.submitRealForPage(val);
      }
    },

    submitRealForPage(val) {
      this.loading = true;
      this.submitWd();
    },
    submitHotWd(index) {
      this.wd = document.getElementById(index).innerText;
      this.submitWd();
    },
    goTop() {
      // 回到顶部
      document.body.scrollTop = document.documentElement.scrollTop = 0;
    },
  },
};
</script>

<style>
/* 解决body和div之间间隔 */
* {
  margin: 0px;
  padding: 0px;
}

.container {
  width: 100%;
  height: 100%;
  z-index: 1;
}
.el-input__inner {
  border-bottom: 2px #cccccc solid;
  border-top: 2px #cccccc solid;
  border-left: 2px #cccccc solid;
  border-right: none;
  border-bottom-left-radius: 10px;
  border-top-left-radius: 10px;
}
.el-input__inner:focus {
  border-bottom: 2px #4e6ef2 solid;
  border-top: 2px #4e6ef2 solid;
  border-left: 2px #4e6ef2 solid;
}
.el-input-group__append {
  border: none !important;
  background-color: white;
}
.el-button {
  color: white !important;
  border-left: none !important;
  border-bottom-left-radius: 0px;
  border-top-left-radius: 0px;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  border: 1px #4e6ef2 solid !important;
  background-color: #4e6ef2 !important;
}
.el-button:hover {
  background-color: #4662d9 !important;
}

.t {
  font-weight: 400;
  font-size: medium;
  margin-bottom: 1px;
  line-height: 1.54;
}

.hot {
  color: #666666;
}
.hot:hover {
  color: blue;
}
em {
  color: brown;
}
.hc_header {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12);
  height: 100px;
  background-color: white;
}
.hc_logo {
  float: left;
  margin-top: -7px;
  padding-left: 10px;
  padding-right: 25px;
}
.hc_hotwd {
  text-align: right;
  padding-top: 35px;
  font-size: 13px;
}
.navbar-collapse {
  flex-basis: 100%;
  flex-grow: 1;
  align-items: center;
}
.navbar-nav {
  display: flex;
  flex-direction: column;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}
.mr-auto,
.mx-auto {
  margin-right: auto !important;
}
.nav-link {
  display: block;
  padding: 0.5rem 1rem;
}
.navbar-nav {
  display: flex;
  flex-direction: column;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}
.hc_contentfooter {
  font-size: 13px;
  text-align: left;
  margin-top: 10px;
}
.hc_page {
  float: left;
  margin-bottom: 40px;
  margin-top: 10px;
  margin-left: 140px;
}
.hc_footer {
  width: 100%;
  background: rgba(0, 0, 0, 0.1);
  height: 40px;
  clear: both;
  color: #666;
  padding-top: 10px;
  font-size: 13px;
  /* position: fixed; */
  bottom: 0px;
  text-align: center;
}
</style>
