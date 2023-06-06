# tuple 元组 只能访问不能修改
tuple_data = (1, 2, 3, 3)
# 元素计数
print(tuple_data.count(3))  # 2
# 输出元素下标
print(tuple_data.index(2))  # 1

# list
arr = [1, 2, 3]
print(type(arr))
# tuple
dictData = (1, 2, 3)
print(type(dictData))
# set
setData = {1, 2, 3}
print(type(setData))
# complex 可以进行复数计算
complex_value1 = 1 + 3j
complex_value2 = 2 - 1j
print(complex_value1 * complex_value2)
# list和tuple互转
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_tuple = tuple(my_list)
print(my_list)
print(my_tuple)
