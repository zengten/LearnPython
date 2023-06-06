# 创建一个set
my_set = set()
# 新增元素
my_set.add('item1')
my_set.add('item2')
my_set.add('item3')
print(my_set)  # {'item2', 'item1', 'item3'}
# 移除一个元素，不存在会报错 KeyError
my_set.remove('item2')  # {'item1', 'item3'}
print(my_set)
# 移除首元素，感觉可以当队列
my_set.pop()
print(my_set)  # {'item3'}
# 批量更新/添加
my_set.update(['item10', 'item11'])
print(my_set)  # {'item11', 'item3', 'item10'}
# set和list互转
my_list = list(my_set)
print(my_list)  # ['item10', 'item11', 'item1']
new_set = set(my_list)
print(new_set)  # ['item10', 'item11', 'item1']
# 批量删除
my_set.clear()
print(my_set)  # set()
# 多个set取交集
my_set1 = {'item1', 'item2', 'item3'}
my_set2 = {'item4', 'item2', 'item5'}
print(my_set1.intersection(my_set2))  # {'item2'}
# 子集和超集函数
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1))  # True
print(st1.issuperset(st2))  # True
# 差集函数
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A.difference(B))  # {1, 2, 3}
print(B.difference(A))  # {8, 6, 7} => A-(A∩B)
print(A.symmetric_difference(B))  # {1, 2, 3, 6, 7, 8}
print(B.symmetric_difference(A))  # {1, 2, 3, 6, 7, 8} => A+B-(A∩B)
# 判断是否有交集
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}
print(set1.isdisjoint(set2))  # True，因为 set1 和 set2 没有交集
print(set1.isdisjoint(set3))  # False，因为 set1 和 set3 有交集

# 删除变量引用
del my_set
# print(my_set)
