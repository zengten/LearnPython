# 定义函数
def add(a, b):
    return a + b


# 调用函数
print(add(1, 2))


# 函数调用函数
def function1():
    i = 10
    print(function2() + i)


def function2():
    return 20


function1()

# 全局变量
c = 100


def function3():
    # 函数内使用global关键字声明全局变量c
    global c
    c = 200
    return c


def function4():
    print(function3() + c)


def function5():
    print(c + function3())


function5()  # 300
function4()  # 400


# 函数的形参和实参
def function6(_d):
    _d += 1
    print(_d)


# 修改形参不会修改实参值
d = 20
function6(d)  # 21
print(d)  # 20

# 但是如果函数传递的是列表，集合字典，函数内部的修改会影响到外部数据
my_array = ['hello', 'world']


def function7(_my_array):
    _my_array[0] = 'haha'


function7(my_array)
print(my_array)  # ['haha', 'world']


# 函数缺省默认值
def function8(_i, _j=1):
    return _i + _j


print(function8(2))  # 3


# 可变参数
def sums(*args):
    n = 0
    for _i in args:
        n += _i
    return n


print(sums(1, 2, 3))  # 6


# 函数作为函数的参数
def function9(_func, *args):
    return _func(*args)


print(function9(sums, 2, 3, 4))  # 9
