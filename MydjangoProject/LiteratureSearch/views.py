import json
from LiteratureSearch import search_utils
from django.http import HttpResponse, JsonResponse


def get(request):
    return HttpResponse("Hello Get")


# 搜索接口
# 请求地址 localhost:8000/search/
# 请求方法 Get
# 参数 搜索关键字 query(string) 必填
# 搜索字段 theme(string) 可选 取值：author,abstract,title
# 页面 page(String) 可选 代表返回的页数
# 排序 order(String) 可选 0时间顺序 1时间逆序
# 年份 year(String) 可选 如果是范围 1997,2007用逗号隔开 否则2020限定年份

def search(request):
    request.encoding = 'utf-8'
    query = request.GET['query']
    # print("OK")
    if 'theme' in request.GET and request.GET['theme']:
        theme = request.GET['theme']
    else:
        theme = None
    if 'page' in request.GET and request.GET['page']:
        page = request.GET['page']
    else:
        page = None
    if 'order' in request.GET and request.GET['order']:
        order = request.GET['order']
    else:
        order = None
    if 'year' in request.GET and request.GET['year']:
        year = request.GET['year']
    else:
        year = None

    result = search_utils.search(query, theme, page, order, year)
    return HttpResponse(json.dumps(result))


# 搜索建议接口
# 请求地址 localhost:8000/search/suggest
# 请求方法 Get
# 参数 keyword 输入的内容
def suggest(request):
    keyword = request.GET['keyword']
    return HttpResponse(json.dumps(search_utils.get_suggestion(keyword)))
