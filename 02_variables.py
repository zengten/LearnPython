import keyword

# 输出python关键词
print(keyword.kwlist)

# int转化为float类型
int_value = 10
print(float(int_value))

# 怎么转化为字符串
int_array = [1, 2, 3, 4]
print(str(int_array))

string = "1234"
# 字符串转化为字符数组
print(list(string))  # ['1', '2', '3', '4']
# 字符串转化为int数组
print(list(map(int, string)))  # [1, 2, 3, 4]

# 格式化输出 5123.00
print("%.2f" % 5123)

# 交换两个变量的值
x = 10
y = 20
x, y = y, x
print(x) # 20
print(y) # 10