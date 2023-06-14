import os
import json
import csv
import xlrd

# reading_file_example文件内容：
"""
hello world1
hello world2
"""
# 文件处理 语法：open(filePath, mode),其中mode默认是读(r)
my_file = open('reading_file_example.txt')
print(my_file)  # <_io.TextIOWrapper name='d:\\test\\reading_file_example.txt' mode='r' encoding='cp936'>
file_read = my_file.read()  # 读取整个文件字符
print(type(file_read))  # <class 'str'>
print(file_read)  # hello world1 \n hello world2
my_file.close()

# 读取固定文件字符
my_file = open('reading_file_example.txt')
file_read = my_file.read(11)  # 读取11个文件字符 hello world
print(file_read)  # hello world
my_file.close()

# 读取整行文件字符
my_file = open('reading_file_example.txt')
file_read = my_file.readline()
print(file_read)  # hello world1
my_file.close()

# 读取多行文件字符，返回字符串数组
my_file = open('reading_file_example.txt')
file_read = my_file.readlines()
print(file_read)  # ['hello world1\n', 'hello world2']
my_file.close()

# 写文件，语法：open(filePath, mode), mode为'a'表示追加写，'w'表示覆盖写，如果文件不存在就创建新文件
with open('reading_file_example.txt', 'a') as f:  # 追加写
    f.write('\nhello world3')
    f.close()

with open('writing_file_example.txt', 'w') as f:  # 覆盖写
    f.write('hello world1')
    f.close()

# 删除文件 os.remove 文件不存在会有 FileNotFoundError
if os.path.exists('writing_file_example.txt'):
    os.remove('writing_file_example.txt')
    print('文件删除成功！')
else:
    print('文件不存在，无需删除！')

# json处理
person_json = '''{
    "name": "zhangSan",
    "city": "ShangHai",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# 将jsonStr转化为字典类型
json_dict = json.loads(person_json)
print(type(json_dict))  # <class 'dict'>
print(json_dict)  # {'name': 'zhangSan', 'city': 'ShangHai', 'skills': ['JavaScrip', 'React', 'Python']}
# 将json_dict转化为json字符串，缩进为4更美观易读
json_str = json.dumps(json_dict, indent=4)
print(type(json_str))  # <class 'str'>
print(json_str)
# output
# {
#     "name": "zhangSan",
#     "city": "ShangHai",
#     "skills": [
#         "JavaScrip",
#         "React",
#         "Python"
#     ]
# }

# 保存json到文件中
with open('json_example.json', 'w', encoding='utf-8') as f:
    # json.dump方法解释：json_dict必填，文件对象f必填，ensure_ascii（可选）将所有非 ASCII 字符转义（默认为 True）
    json.dump(json_dict, f, ensure_ascii=False, indent=4)
    f.close()

# 读入csv文件
with open('csv_example.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'表头为{row}')
            line_count += 1
        else:
            print(f'数据为{row}')
    # output
    """表头为['姓名', '性别', '年龄', '爱好']
    数据为['ZhangSan', '男', '23', 'JavaScript']
    数据为['LiSi', '女', '28', 'Python']"""

# 读入excel表格，xlrd只支持早期的xls格式表格
try:
    excel_book = xlrd.open_workbook('excel_xls_example.xls')
    print(excel_book.nsheets)  # 3
    print(excel_book.sheet_names())  # ['人员表', 'Sheet2', 'Sheet3']
    sheet0 = excel_book.sheet_by_index(0)
    for row in sheet0:
        print(row)
    # [text: '姓名', text: '性别', text: '年龄', text: '爱好']
    # [text: '张三', text: '男', number: 22.0, text: 'Java']
    # [text: '李四', text: '女', number: 35.0, text: 'Python']
except Exception as e:
    print(f'读取excel出现错误，{e}')
