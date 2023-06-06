# 条件语句
int_value = 0
if int_value > 0:
    print("正数")
elif int_value < 0:
    print("负数")
else:
    print("零")

# pass 空语句，它并不执行任何操作，只是占据一行位置
if int_value == 0:
    pass
else:
    print(int_value)

# while循环
i = 0
n = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    if i == 5:
        break
    n += i
print(n)  # 8

# for循环
language = ['python', 'Java', 'C++']
for item in language:
    print(item)
# range函数，用于生成一个整数序列，
# 三个参数 start：序列起始值，默认为 0。
# stop：序列结束值，不包括该值。
# step：序列的步长，默认为 1。
for i in range(3):
    print(language[i])
for i in range(len(language)):
    print(language[i])
for i in range(0, 10, 2):
    print(i)  # 0,2,4,6,8
# 遍历字典
person = {
    'name': 'zhangSan',
    'skill': ['Java', 'C++', 'Python'],
    'address': {'k1': 'v1', 'k2': 'v2'}
}
for key, value in person.items():
    print('key:{},value:{}'.format(key, value))
# for结束时进行else输出
for number in range(3):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops')
