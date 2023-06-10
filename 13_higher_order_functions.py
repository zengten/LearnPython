import functools


# 闭包：允许内部函数访问封闭函数的外部作用域
def add_one():
    i = 1

    def add(num):
        return num + i

    # 返回定义的函数
    return add


print(add_one()(10))  # 11
print(add_one()(20))  # 21
one = add_one()
print(one(10))  # 11
print(one(20))  # 21


def add_two():
    i = 1

    def add(num):
        # 声明非本地变量
        nonlocal i
        i += 1
        return num + i

    # 返回定义的函数
    return add


# 同个闭包函数连续调用，结果不一致，因为闭包函数内部缓存了变量值
counter = add_two()
print(add_two()(10))  # 12
print(add_two()(20))  # 22
print(counter(10))  # 12
print(counter(20))  # 23


# 使用闭包调用，实现装饰
def greeting1():
    return 'Welcome to Python'


def uppercase_decorator(function):
    def wrapper():
        print('uppercase_decorator')
        func = function()
        uppercase_str = func.upper()
        return uppercase_str

    return wrapper


# 注意uppercase_decorator(greeting1)返回函数，还需要继续调用
print(uppercase_decorator(greeting1)())  # WELCOME TO PYTHON


# 装饰器实现
@uppercase_decorator
def greeting2():
    return 'Welcome to Python'


print(greeting2())  # WELCOME TO PYTHON


def split_decorator(func):
    def wrapper():
        print('split_decorator')
        return func().split()

    return wrapper


# 多个装饰器实现，执行顺序：split_decorator -> uppercase_decorator
@split_decorator
@uppercase_decorator
def greeting3():
    return 'Welcome to Python'


print(greeting3())  # ['WELCOME', 'TO', 'PYTHON']


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(param1, param2, city):
        function(param1, param2, city)
        print("I am live in {}".format(city))  # I am live in shenZheng

    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, city):
    # I am zhang san, no live desc
    print('I am {} {}, no live desc'.format(first_name, last_name, city))


# 装饰器方法必须写在实际调用方法之前，TODO 怎么装饰一个import的方法
print_full_name("zhang", "san", "shenZheng")

# lambda函数map使用，基本格式 map(function, iterator)
my_list = [1, 2, 3, 4, 5]
# 实现每个元素平方，map转化之后，再转成list
print(list(map(lambda x: x ** 2, my_list)))  # [1, 4, 9, 16, 25]
# int数组 -> 字符数组
print(list(map(str, my_list)))  # ['1', '2', '3', '4', '5']
# 字符数组 -> int数组
my_list = ['1', '2', '3', '4', '5']
print(list(map(int, my_list)))  # [1, 2, 3, 4, 5]
# 字符串数组转化为大写
my_list = ['welcome', 'to', 'python']
print(list(map(str.upper, my_list)))  # ['WELCOME', 'TO', 'PYTHON']
# 字符串数组转化为大写，然后拼接
print(' '.join(list(map(str.upper, my_list))))  # WELCOME TO PYTHON

# filter使用，语法：filter(function, iterator)
my_list = [1, 2, 3, 4, 5]


def is_odd(_x):
    return _x & 1 == 1


# 过滤偶数
print(list(filter(is_odd, my_list)))  # [1, 3, 5]
# 过滤奇数
print(list(filter(lambda x: x % 2 == 0, my_list)))  # [2, 4]

# reduce使用，语法 reduce(function, iterator)
my_list = ['1', '2', '3', '4', '5']
total = functools.reduce(lambda _x, _y: int(_x) + int(_y), my_list)  # TODO warnings
print(total)  # 15
