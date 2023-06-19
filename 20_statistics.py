import numpy as np

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
