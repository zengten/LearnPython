import pandas as pd
import numpy as np

nums = [1, 2, 3, 4, 5]
print(pd.array(nums))  # <IntegerArray> [1, 2, 3, 4, 5] Length: 5, dtype: Int64

# 使用list创建 Pandas Series，有点像excel表格
hobby_list = ['sing', 'jump', 'basketball']
print(pd.Series(hobby_list, index=[1, 2, 3]))
# output
# 1          sing
# 2          jump
# 3    basketball
# dtype: object

# 使用dict创建 Pandas Series
person_info = {'name': 'ZhangSan', 'age': 22, 'gender': '男'}
print(pd.Series(person_info))
# output
# name      ZhangSan
# age             22
# gender           男
# dtype: object

# 使用单个字符创建 Pandas Series
print(pd.Series('love', index=[1, 2, 3]))
# output
# 1    love
# 2    love
# 3    love
# dtype: object

# 使用numpy的linspace创建 Pandas Series
print(pd.Series(np.linspace(1, 5, 5)))
# output
# 0    1.0
# 1    2.0
# 2    3.0
# 3    4.0
# 4    5.0
# dtype: float64

# 使用二维数组 创建 DataFrame
list_of_list = [['ZhangSan', '男', '22'], ['LiSi', '女', '25'], ['WangWu', '未知', '29']]
data_frame = pd.DataFrame(list_of_list, columns=['姓名', '性别', '年龄'])
print(data_frame)
# output
#          姓名  性别  年龄
# 0  ZhangSan   男  22
# 1      LiSi   女  25
# 2    WangWu  未知  29

# 使用字典 创建 DataFrame
person_dict = {'姓名': ['ZhangSan', 'LiSi', 'WangWu'], '性别': ['男', '女', '未知'], '年龄': ['22', '25', '29']}
print(pd.DataFrame(person_dict))  # 输出和上面一致

# pandas读取csv文件
pd_read_csv = pd.read_csv('csv_example.csv')
print(pd_read_csv.head())  # 输出前5行数据
print(pd_read_csv.tail())  # 输出后5行数据
print(pd_read_csv.shape)  # 输出总体数据(行, 列)  (2, 4)
print(pd_read_csv.columns)  # 输出数据的表头 Index(['姓名', '性别', '年龄', '爱好'], dtype='object')
csv_name_column = pd_read_csv['姓名']
print(csv_name_column)  # 输出key一列数据
print(csv_name_column.describe())  # 输出一列数据的格式，包括宽度高度等
print(pd_read_csv)

# pandas读取旧版excel文件，需要额外安装库 xlrd
pd_read_excel = pd.read_excel('excel_xls_example.xls')
print(pd_read_excel)

# pandas读取新版excel文件，需要额外安装库 openpyxl
pd_read_excel = pd.read_excel('excel_xlsx_example.xlsx', engine='openpyxl')
print(pd_read_excel)

#
data = [
    {"姓名": "ZhangSan", "性别": "男"},
    {"姓名": "LiSi", "性别": "女"},
    {"姓名": "WangWu", "性别": "未知"}]
df = pd.DataFrame(data)
print(df)
# DataFrame 中添加列
df['爱好'] = ['唱', '跳', 'rap']
print(df)
# DataFrame 中添加 Weight和Height
df['Weight'] = [74, 78, 69]
df['Height'] = [173, 175, 169]
# 换算height单位
df['Height'] = df['Height'] * 0.01


def calculate_bmi(_df):
    weights = _df['Weight']
    heights = _df['Height']
    _bmi = []
    for w, h in zip(weights, heights):
        _bmi.append(w / (h * h))
    return _bmi


# 通过身高和体重计算BMI
bmi = calculate_bmi(df)
print(bmi)
df['BMI'] = bmi
print(df)
df['BMI'] = round(df['BMI'], 2)  # bmi值保留2位小数
print(df)

# 加入出生年，然后计算年龄
birth_year = ['1969', '1985', '1990']
df['Birth Year'] = birth_year
df['Current Year'] = ['2023', '2023', '2023']
# 直接计算会报错，因为都是字符串
# ages = df['Current Year'] - df['Birth Year']
ages = df['Current Year'].astype(int) - df['Birth Year'].astype(int)
print(ages)
# output
# 0    54
# 1    38
# 2    33
# dtype: int32
df['Ages'] = ages
print(df)
# output
#          姓名  性别   爱好  Weight  Height    BMI Birth Year Current Year  Ages
# 0  ZhangSan   男    唱      74    1.73  24.73       1969         2023    54
# 1      LiSi   女    跳      78    1.75  25.47       1985         2023    38
# 2    WangWu  未知  rap      69    1.69  24.16       1990         2023    33

# 过滤输出数据
print(df[df['Ages'] > 40])
# output
#          姓名 性别 爱好  Weight  Height    BMI Birth Year Current Year  Ages
# 0  ZhangSan  男  唱      74    1.73  24.73       1969         2023    54
print(df[df['Ages'] < 40])
# output
#        姓名  性别   爱好  Weight  Height    BMI Birth Year Current Year  Ages
# 1    LiSi   女    跳      78    1.75  25.47       1985         2023    38
# 2  WangWu  未知  rap      69    1.69  24.16       1990         2023    33
