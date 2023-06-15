import numpy
import webbrowser
import requests
import json

# 安装导入numpy包  pip install numpy
print(numpy.version.version)  # 1.24.3
my_list = [1, 2, 3, 4, 5]
numpy_array = numpy.array(my_list)
print(numpy_array)  # [1 2 3 4 5]
print(numpy_array * 2)  # [ 2  4  6  8 10]
print(numpy_array + 2)  # [3 4 5 6 7]
print([i for i in numpy_array * 2])  # [2, 4, 6, 8, 10]

# 安装导入pandas包  pip install pandas

# list of urls: python
url_lists = [
    'https://www.python.org',
    'https://www.baidu.com'
]

# 使用 webbrowser 可以直接打开电脑默认浏览器新窗口
for url in url_lists:
    webbrowser.open_new_tab(url)

# 不使用代理
cur_proxy = {
    'http': None,
    'https': None
}
# 访问该网站
url = 'https://v1.hitokoto.cn/?c=i'
try:
    response = requests.get(url, proxies=cur_proxy)
    print(response)
    print(response.status_code)
    print(response.text)  # 整个网页
    print(type(response.json()))  # <class 'dict'>
    # ensure_ascii = True 会将中文进行 unicode编码
    print(json.dumps(response.json(), ensure_ascii=False, indent=4))  # 格式化输出
except Exception as e:
    print(f'出现error{e}')
