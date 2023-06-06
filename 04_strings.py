# 多行字符串
multiline_string = '''line1.
line2.
line3.'''
print(multiline_string)
# 另外一种表示方式
multiline_string = """line1.
line2.
line3."""
print(multiline_string)

language = 'Python'
# 字符赋值方式
a, b, c, d, e, f = language
print(a)  # P
print(b)  # y
# 正序第三个字符
print(language[2])  # t
# 逆序第一个字符
print(language[-1])  # n
# 子串 str[a:b:c]，返回str从a到b子串,c长度
print(language[0:3])  # Pyt
print(language[3:])  # hon
print(language[-3:])  # hon
print(language[0:3:2])  # Pt

str1 = 'third of python learn'
print(str1.capitalize())  # 首字母大写
print(str1.upper())  # 全部字符大写
print(str1.count('t'))  # 计数t字符
print(str1.endswith('learn'))  # 是否以该字符结尾

str1 = 'third\tof\tpython\tlearn'
print(str1)
print(str1.expandtabs())
print(str1.expandtabs(10))

print('hello1'.isalnum())  # 是字符或者数值
print('hello1'.isalpha())  # 是字符
print('123'.isdigit())  # 只能判断纯数字字符，即 "0" 至 "9"，对于小数点、负数等均不支持
print('123'.isdecimal())  # 用于判断字符串是否只包含十进制数字字符，即 "0" 至 "9"。不支持小数点、负数、以及其他数字字符
print('123'.isnumeric())  # 更加宽泛，可以判断是否为数字字符，包括汉字数字、罗马数字等。但同样不支持小数点、负数等。
print('hello'.islower())  # 是否小写
print('hello'.isidentifier())  # 是否合法python字符串，不能数值开头
print('Hello'.istitle())  # 是否标题，首字符大写
print('hello world'.title())  # 将单词首字母都改成大写 Hello World
# 字符串格式化输出
print('he{}wor{}'.format('llo', 'ld'))

language = ['HTML', 'JAVA', 'C++']
#  数组拼接成字符串，使用&,隔开
print('&,'.join(language))  # HTML&,JAVA&,C++

print('  hello world  '.strip())  # 去除首尾空格，中间空格不会去除
print('HELLO world'.swapcase())  # 大小写字母互换，hello WORLD

# 输入
# input_str = input("请输入字符串：")
# print(input_str)
