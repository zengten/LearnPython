# 语法 [i for i in iterable if expression]
language = 'Python'
# 第一种方式将字符串转换为字符数组
my_list = list(language)
print(type(my_list))
print(my_list)
# 第二种方式
my_list = [i for i in language]
print(type(my_list))
print(my_list)

# 生成list数据，元素/元组
print([i for i in range(5)])  # [0, 1, 2, 3, 4]
print([i * i for i in range(5)])  # [0, 1, 4, 9, 16]
print([(i, i * i) for i in range(5)])  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
# 偶数和奇数
print([i for i in range(10) if i % 2 == 0])  # [0, 2, 4, 6, 8]
print([i for i in range(10) if i % 2 != 0])  # [1, 3, 5, 7, 9]
# 按条件筛选数组
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
print([i for i in numbers if i % 2 == 0 and i > 0])  # [4, 6, 8, 10]
# 操作二维数组
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([number for row in list_of_lists for number in row])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# lambda函数
def add_two_nums(_f, _x, _y):
    print(_f(_x, _y))


add_two_nums(lambda _x, _y: _x + _y, 1, 2)  # 3

# lambda函数自己调用自己
print((lambda _x, _y: _x + _y)(2, 3))  # 5


# lambda在另外一个函数内部
def power(_x):
    # 返回一个参数的lambda函数
    return lambda _n: _x ** _n


print(power(2)(3))  # 2 ** 3 = 8
