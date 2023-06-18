fruits = ['apple', 'orange']
print(fruits)  # ['apple', 'orange']
# 末尾添加元素
fruits.append('banana')
print(fruits)  # ['apple', 'orange', 'banana']
# 指定位置添加元素
fruits.insert(1, 'lemon')
fruits.insert(1, 'lemon')
print(fruits)  # ['apple', 'lemon', 'lemon', 'orange', 'banana']
# 移除元素，相同元素只会移除一个
fruits.remove('lemon')
print(fruits)  # ['apple', 'lemon', 'orange', 'banana']
# 移除指定位置元素
fruits.pop(2)
print(fruits)  # ['apple', 'lemon', 'banana']
# 移除末尾元素
fruits.pop()
print(fruits)  # ['apple', 'lemon']
# del关键字删除对象引用
del fruits[1]
print(fruits)  # ['apple']
# copy
fruits = ['apple', 'lemon', 'banana']
print(fruits.copy())  # ['apple', 'lemon', 'banana']
# 数组拼接
num1 = [1, 2, 3]
num2 = [4, 5]
print(num1 + num2)  # [1, 2, 3, 4, 5]
# 数组继承
arr1 = ['a', 'b', 'c']
arr2 = ['d', 'e']
arr1.extend(arr2)
print(arr1)  # ['a', 'b', 'c', 'd', 'e']
# 数组元素计数
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))  # 3
# 数组下标，多个相同元素返回第一个下标
print(ages.index(24))  # 2
# 数组反转
fruits = ['apple', 'lemon', 'banana']
fruits.reverse()  # 无返回
print(fruits)  # ['banana', 'lemon', 'apple']
# 数组排序
my_list = [3, 1, 4, 5, 9]
my_list.sort()  # 原有列表排序
print(my_list)  # [1, 3, 4, 5, 9]
my_list.sort(reverse=True)  # 逆序排序
print(my_list)  # [9, 5, 4, 3, 1]
my_list = [3, 1, 4, 5, 9]
new_list = sorted(my_list)  # 返回新的排序列表
print(new_list)  # [1, 3, 4, 5, 9]
new_list = sorted(my_list, reverse=True)  # 逆序排序
print(new_list)  # [9, 5, 4, 3, 1]

# 数组遍历 -> enumerate函数：用于在循环中同时获取元素和元素的索引
names = ['ZhangSan', 'LiSi', 'WangWu']
for index, name in enumerate(names):
    print(f'index={index}, name = {name}')

del fruits
print(fruits)  # name 'fruits' is not defined
