from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# 时间+日期
today = datetime.now()
# 年月日 时分秒 格式输出  2023-6-10 20:36:7
print(f'{today.year}-{today.month}-{today.day} {today.hour}:{today.minute}:{today.second}')
print(today.timestamp())  # 1686400611.387102
print(datetime(2022, 2, 3))  # 2022-02-03 00:00:00
# 日期格式化 strftime 函数
print(today.strftime('%Y-%m-%d %H:%M:%S'))  # 2023-06-10 21:19:48
print(today.strftime('%y-%m-%d %H:%M:%S'))  # 23-06-10 21:19:48
# 字符串转日期 strptime 函数, strptime(str_date, str_format)
date_string = "5 December, 2019"
print(datetime.strptime(date_string, '%d %B, %Y'))  # 2019-12-05 00:00:00
print(datetime.strptime('2023-06-10 21:19:48', '%Y-%m-%d %H:%M:%S'))  # 2023-06-10 21:19:48

# 日期
today = date.today()
print(today)  # 2023-06-10
print(today.strftime('%x'))  # 06/10/23

# 时间
cur_time = time()
print(cur_time)  # 00:00:00
cur_time = time(10, 22, 33)
print(f'{cur_time.hour}:{cur_time.minute}:{cur_time.second}')  # 10:22:33

# 日期差
date1 = date(2022, 1, 29)
date2 = date(2022, 2, 2)
print(date2 - date1)  # 4 days, 0:00:00

# 时间差
datetime1 = datetime(year=2022, month=1, day=2, hour=10, minute=30, second=22)
datetime2 = datetime(year=2022, month=1, day=3, hour=11, minute=32, second=32)
print(datetime2 - datetime1)  # 1 day, 1:02:10

# 计算时间差
today = datetime.now()
print(today)  # 2023-06-10 23:45:42.107976
# 2小时前
two_hour_ago = today - timedelta(hours=2)
print(two_hour_ago)  # 2023-06-10 21:45:42.107976
# 3天后
three_days_ago = today + timedelta(days=3)
print(three_days_ago)  # 2023-06-13 23:45:42.107976
