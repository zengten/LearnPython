import os
import sys
import math
import string
import random
import warnings

# 导入其他模块的代码，进行调用
from my_module import generate_full_name, sum_two_nums as sums

print(generate_full_name('liu', 'yi fei'))  # liu yi fei
print(sums(1, 2))  # 3

# 创建文件夹
if os.path.exists('test_dir'):
    print('test_dir目录已存在！')
else:
    os.mkdir('test_dir')
# 删除文件夹
os.rmdir('test_dir')
# 更改工作目录（读写文件）
os.chdir('c://')
# 获取当前工作目录
print(os.getcwd())

# 输出当前文件目录，执行命令参数
print(sys.argv)  # ['E:\\project\\PythonProject\\LearnPython\\11_modules.py']
print(sys.maxsize)  # 9223372036854775807
print(sys.version)  # 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)]

# 数学函数
print(math.pi)  # 3.141592653589793
print(math.sqrt(2))  # 1.4142135623730951
print(math.pow(26, 2))  # 676.0
print(math.floor(2.1))  # 2

# string模块 TODO 怎么抑制警告
warnings.filterwarnings('ignore')
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.whitespace)  # 空白字符

# random模块
print(random.random())  # 随机数0~1
print(random.randint(5, 20))  # 随机整数5~20
