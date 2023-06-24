import numpy as np
import matplotlib.pyplot as plt

python_list = [1, 2, 3, 4, 5]
# 创建int数组对象
numpy_list = np.array(python_list)
print(type(numpy_list))  # <class 'numpy.ndarray'>
print(numpy_list)  # [1 2 3 4 5]
# 重新转回python_list
print(type(numpy_list.tolist()))  # <class 'list'>

# 创建float数组对象
numpy_float_list = np.array(python_list, dtype=float)
print(numpy_float_list)  # [1. 2. 3. 4. 5.]

# 创建bool数组对象
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)  # [False  True  True False False]

np_array = np.array([1, 2, 3, 4, 5])
print(np_array.shape)  # (5,) 一维5元素
print(np_array.dtype)  # int32

three_by_four_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
print(three_by_four_array.shape)  # (3, 4)  三行四列

# numpy的加减乘除 向下取整 取余 指数 运算
numpy_list = np.array([1, 2, 3, 4, 5])
print(numpy_list + 2)  # [3 4 5 6 7]
print(numpy_list - 1)  # [0 1 2 3 4]
print(numpy_list * 2)  # [ 2  4  6  8 10]
print(numpy_list / 2)  # [0.5 1.  1.5 2.  2.5]
print(numpy_list // 2)  # [0 1 1 2 2]
print(numpy_list % 2)  # [1 0 1 0 1]
print(numpy_list ** 2)  # [ 1  4  9 16 25]

# 切片 [0:2, 0:2]表示二维里的 0-1行 0-1列
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dimension_array[:3, :3])  # 二维里的三行三列，就是输出原数组

# numpy数组元素类型转换
numpy_list = np.array([1, 2, 3, 4, 5])
# 1.int to float
print(numpy_list.astype(dtype=float))  # [1. 2. 3. 4. 5.]
# 2.int to str
print(numpy_list.astype(dtype=str))  # ['1' '2' '3' '4' '5']
# 3.int to bool
print(numpy_list.astype(dtype=bool))  # [ True  True  True  True  True]

# 二维数组
two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 一行一行输出
print(two_dimension_array[0])  # [1 2 3]
print(two_dimension_array[1])  # [4 5 6]
print(two_dimension_array[2])  # [7 8 9]
# 一列一列输出
print(two_dimension_array[:, 0])  # [1 4 7]
print(two_dimension_array[:, 1])  # [2 5 8]
print(two_dimension_array[:, 2])  # [3 6 9]
# 翻转行和列
print(two_dimension_array[::-1])  # 翻转行 [[7 8 9][4 5 6][1 2 3]]
print(two_dimension_array[:, ::-1])  # 翻转列 [[3 2 1][6 5 4][9 8 7]]
print(two_dimension_array[::-1, ::-1])  # 翻转行和列 [[9 8 7][6 5 4][3 2 1]]
# 填充二维数组元素值
two_dimension_array[1, 1] = 10
print(two_dimension_array)  # [[ 1  2  3][ 4 10  6][ 7  8  9]]

# 自动填充数组，使用0填充一个2行3列数组，默认类型是float
two_three_array = np.zeros((2, 3))
print(two_three_array)  # [[0. 0. 0.] [0. 0. 0.]]
# 1行三列数组，int类型
one_three_array = np.zeros((1, 3), dtype=int)
print(one_three_array)  # [[0 0 0]]
# 另外还有 使用1自动填充的数组
np_ones = np.ones((1, 3), dtype=int)
print(np_ones)  # [[1 1 1]]

# 数组转化变形
first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print(first_shape)
# 2行3列 -> 3行2列
reshape_array = first_shape.reshape(3, 2)
print(reshape_array)  # [[1 2][3 4][5 6]]
# 将二维数组转化为一维数组  TODO  怎么ide不提示这个方法
array_flatten = reshape_array.flatten()
print(array_flatten)  # [1 2 3 4 5 6]

# 合并两个数组
python_list_one = [1, 2, 3]
python_list_two = [4, 5, 6]
# python类型数组相加
print(python_list_one + python_list_two)  # [1, 2, 3, 4, 5, 6]
np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])
# numpy类型数组 直接相加
print(np_list_one + np_list_two)  # [5 7 9]
# numpy类型数组合并一维数组,有两个括号
print(np.hstack((np_list_one, np_list_two)))  # [1 2 3 4 5 6]
# numpy类型数组合并成二维数组
print(np.vstack((np_list_one, np_list_two)))  # [[1 2 3][4 5 6]]

# numpy生成随机数
np_random = np.random.random()  # 生成1个0-1随机数
print(np_random)
np_random = np.random.random(5)  # 生成5个0-1随机数组
print(np_random)
np_random = np.random.randint(2, 10, size=4)  # 生成2-10内4个随机数 [4 9 7 6]
print(np_random)
np_random = np.random.randint(2, 10, size=(2, 2))  # 生成2-10内 2*2二维数组随机数
print(np_random)
# 生成一个均值为 2，标准差为 1，形状为 (3, 4) 的随机数组
np_random = np.random.normal(2, 1, size=(3, 4))
print(np_random)

# 矩阵
matrix = np.matrix(np.ones((4, 4), dtype=int))
print(matrix)  # 输出4*4矩阵

# numpy的range方法，跟python自身的差不多
odd_list = np.arange(1, 10, 2)
print(odd_list)  # 输出奇数[1 3 5 7 9]
even_list = np.arange(2, 10, 2)
print(even_list)  # 输出偶数[2 4 6 8]

# numpy.linspace(start, end, size) 指定范围内生成均匀间隔数组
np_array = np.linspace(1, 10, 3, dtype=int)
print(np_array)  # [ 1  5 10]
# numpy.logspace(start, end, size) 指定范围生成均匀个数 对数数组，默认10为底
np_array = np.logspace(1, 3, 3)
print(np_array)  # [  10.  100. 1000.]
print(np.logspace(1, 5, 5, base=2))  # [ 2.  4.  8. 16. 32.] 2为底

# 统计分析函数
np_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 1.最大数，最小数，平均数
print(np_array.max())  # 9
print(np_array.min())  # 1
print(np_array.mean())  # 5.0
print(np.median(np_array))  # 中位数 5.0
print(np_array.std())  # 标准差 2.581988897471611
print(np.amin(np_array, axis=0))  # axis = 0 计算每列的最小值 [1 2 3]
print(np.amin(np_array, axis=1))  # axis = 1 计算每行的最小值 [1 4 7]

# 创建重复序列  np.repeat(array, n) 重复 n-1 次
my_array = [1, 2, 3]
print(np.repeat(my_array, 2))  # 每个元素重复一次 [1 1 2 2 3 3]
print(np.tile(my_array, 2))  # 整个序列重复一次 [1 2 3 1 2 3]

# 计算矩阵乘法
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))

# 绘制图形坐标轴
x = np.array([0, 1, 2, 3, 4])
# 相当于坐标函数
y = x * 2
plt.plot(x, y)
# x轴文字描述
plt.xlabel('x')
# y轴文字描述
plt.ylabel('y')
# 标题文字描述
plt.title('test')
# x轴刻度值
plt.xticks(np.arange(0, 6, step=1))
plt.show()
