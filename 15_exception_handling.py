from itertools import zip_longest

# 异常处理
try:
    print(1 + '2')
except TypeError:
    print('TypeError occurred')

try:
    value = 1 / 0
except ZeroDivisionError:
    print('ZeroDivisionError occurred')

# 捕获所有异常进行输出
try:
    my_list = [1, 2, 3]
    print(my_list[3])
except Exception as e:
    print(e)  # list index out of range

# 多级异常捕获
try:
    # 默认输入都是字符串
    name = input("请输入你的姓名：")
    born_in = input("请输入你的出生年：")
    # 必须转化类型
    age = 2023 - int(born_in)
    print(age)
    print(f'you are {name}, and your age is {age}')
except TypeError:
    print('TypeError occurred')
# 转化类型失败会出现 ValueError
except ValueError:
    print('ValueError occurred')
# 未出现Error则会执行else
else:
    print('else code exec...')
# 最终都会执行的finally
finally:
    print('finally code exec...')


# 解包和打包,元组和数组使用'*',字典使用'**'
def unpacking_tuple(_name, _age, _city):
    print(f'my name is {_name}, I am {_age} years old, I am from {_city}')


def packing_tuple(*args):
    for item in args:
        print(item)


person = ('ZhangSan', 22, 'ShangHai')
# 直接调用会出现TypeError, 此时需要对元组进行解包(*person)
# print_person(person)
unpacking_tuple(*person)  # my name is ZhangSan, I am 22 years old, I am from ShangHai
# 参数打包
packing_tuple('ZhangSan', 22, 'ShangHai')


# 字典解包
def unpacking_dict(_name, _age, _city):
    print(f'my name is {_name}, I am {_age} years old, I am from {_city}')


# 字典打包
def packing_dict(**args):
    for key in args:
        print(f'key = {key}, value = {args[key]}')


person = {'_name': 'zhangSan', '_age': 22, '_city': ['ShangHai', 'BeiJin']}
unpacking_dict(**person)
packing_dict(_name='zhangSan', _age=22, _city=['ShangHai', 'BeiJin'])

# 合并多个集合
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
combine_list = [0, *my_list1, *my_list2]
print(combine_list)  # [0, 1, 2, 3, 4, 5, 6]
# 合并多个字典
my_dict1 = {'name': 'zhangSan', 'hobby': ['sing', 'jump']}
my_dict2 = {'age': 22, 'hobby': ['basketball', 'jump']}
combine_dict = {**my_dict1, **my_dict2}
# 一个键在多个字典中都存在，只保留最后一个字典值
print(combine_dict)  # {'name': 'zhangSan', 'hobby': ['basketball', 'jump'], 'age': 22}

# enumerate函数：用于在循环中同时获取元素和元素的索引
names = ['ZhangSan', 'LiSi', 'WangWu']
for index, name in enumerate(names):
    print(f'index={index}, name = {name}')
# index=0, name = ZhangSan
# index=1, name = LiSi
# index=2, name = WangWu

# zip函数 将多个可迭代对象打包成一个元组构成的可迭代对象
numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd']
for number, letter in zip(numbers, letters):
    print(f'{number}:{letter}')  # 1:a  2:b  3:c  4:d

# zip可以直接将两个数组合成字典
letter_number_dict = dict(zip(letters, numbers))
print(letter_number_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 当各个迭代器的长度不同时，默认选择最短长度
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd']
for number, letter in zip(numbers, letters):
    print(f'{number}:{letter}')  # 1:a  2:b  3:c  4:d

# 另外可以使用 itertools.zip_longest() 函数 选择最长长度
for number, letter in zip_longest(numbers, letters):
    print(f'{number}:{letter}')  # 1:a  2:b  3:c  4:d  5:None
