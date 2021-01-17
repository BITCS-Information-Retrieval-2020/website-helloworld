<template>
  <div>
    <el-container
      style="position: absolute; height: 70%; width: 100%"
      direction="vertical"
    >
      <el-card class="box-card">
        <el-form ref="form" :model="form" label-width="80px" :rules="rules">
          <b>请输入搜索信息</b>
          <el-form-item label="作者" style="margin-top: 15px" prop="author">
            <el-input v-model="form.author"></el-input>
          </el-form-item>
          <el-form-item label="题目" prop="title">
            <el-input v-model="form.title"></el-input>
          </el-form-item>
          <el-form-item label="逻辑关系" prop="status">
            <el-radio-group v-model="form.status">
              <el-radio label="and"></el-radio>
              <el-radio label="or"></el-radio>
              <el-radio label="not"></el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="检索时间">
            <el-date-picker
              v-model="form.date"
              type="monthrange"
              range-separator="至"
              start-placeholder="开始月份"
              end-placeholder="结束月份"
              value-format="yyyy"
            ></el-date-picker>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit('form')">搜索</el-button>
            <el-button @click="reset">重置</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </el-container>
  </div>
</template>


<script>
export default {
  name: "advancedsearch",
  data() {
    return {
      form: {
        author: "",
        title: "",
        status: "",
        date: "",
      },
      rules: {
        author: [{ required: true, message: "请输入作者", trigger: "blur" }],
        title: [{ required: true, message: "请选择标题", trigger: "blur" }],
        status: [{ required: true, message: "请选择逻辑", trigger: "change" }],
      },
    };
  },
  methods: {
    onSubmit(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // alert("submit!");
          this.$router.push({
            path: "/search",
            query: { form: this.form },
          });
        } else {
          // alert("输入不合法!");
        }
      });
    },
    reset() {
      this.form.author=""
      this.form.title=""
      this.form.status=""
      this.form.date=""
    },
    search() {},
    getList() {
      // addDateRange 方法在 main.js中全局挂载
      listUser(this.addDateRange(this.queryParams, this.dateRange)).then(
        (response) => {
          this.userList = response.rows;
          this.total = response.total;
          // this.loading = false;
        }
      );
    },
    /** 搜索按钮操作 */
    handleQuery() {
      console.log(this.queryParams);
    },
    /** 重置按钮操作 */
    resetQuery() {
      this.dateRange = [];
      this.resetForm("queryForm");
      console.log;
    },
  },
  created() {
    this.getList();
    this.getDicts("sys_normal_disable").then((response) => {
      this.statusOptions = response.data;
    });
  },
  mounted() {},
};
</script>
<style scoped>
.box-card {
  margin: auto;
  width: 500px;
}
.app-container {
  width: 100%;
  max-width: 1000px;
  margin: auto;
  padding: 0%;
}
</style>
