import re
from collections import Counter

txt = 'I love to learn python and javascript'
# 正则表达式 语法：r'正则' ，re.I 忽略大小写   re.M 匹配多行
match_obj = re.match('I love to learn python', txt, re.I)
if match_obj:
    print(match_obj)  # <re.Match object; span=(0, 22), match='I love to learn python'>
    # 获取匹配到的位置
    print(match_obj.span())  # (0, 22)
    start, end = match_obj.span()
    print(txt[start:end])  # I love to learn python
    # 获取匹配到的数据内容
    print(match_obj.group())  # I love to learn python
else:
    print('no match')

# 忽略大小写匹配 Hello
txt = 'hello world'
match_obj = re.match(r'Hello', txt, re.I)
print(match_obj)  # <re.Match object; span=(0, 5), match='hello'>

# 对比match和search方法，world 匹配不到因为txt不符合world正则
txt = 'hello world'
match_obj = re.match('world', txt, re.I)
print(match_obj)  # None

txt = 'hello world'
match_obj = re.search('world', txt, re.I)
print(match_obj)  # <re.Match object; span=(6, 11), match='world'>

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# findall方法返回数组
matches = re.findall('Python', txt, re.I)
print(matches)  # ['Python', 'python']
match_obj = re.findall(r'[Pp]ython', txt)
print(match_obj)  # ['Python', 'python']

# 正则替换
txt = 'Python is the most beautiful language，I like python'
match_obj = re.sub('[Pp]ython', 'Java', txt)  # 将python字符串替换为java
print(match_obj)  # Java is the most beautiful language，I like Java

# 替换字符串百分号
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

match_obj = re.sub('%', '', txt)
print(match_obj)
'''I am teacher and  I love teaching. 
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs. 
Does this motivate you to be a teacher?'''

# 字符串分割
txt = 'I am teacher and I love teaching.'
re_split = re.split(' ', txt)
print(re_split)  # ['I', 'am', 'teacher', 'and', 'I', 'love', 'teaching.']

# 正则匹配
regex_pattern1 = r'\d'  # 匹配单个数值字符
regex_pattern2 = r'\d+'  # 匹配数字
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern1, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']
matches = re.findall(regex_pattern2, txt)
print(matches)  # ['6', '2019', '8', '2021']

# 找出下面段落中，最常见的单词？
paragraph = '''I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you 
all the capabilities to develop an application what else can you love.'''

# \w匹配所有字母数字下划线，\s匹配所有非空白字符，包括换行
paragraph = re.sub(r'\W', ' ', paragraph)  # 匹配所有不是\w字符，用空格替换
print(paragraph)
paragraph_split = paragraph.split()
print(paragraph_split)
# 使用Counter计数
most_common = Counter(paragraph_split).most_common()
print(most_common)
# [('love', 6), ('you', 5), ('can', 3), ('I', 2), ('teaching', 2), ('do', 2),
# ('not', 2), ('what', 2), ('else', 2), ('If', 1), ('Python', 1), ('if', 1),
# ('something', 1), ('which', 1), ('give', 1), ('all', 1), ('the', 1), ('capabilities', 1),
# ('to', 1), ('develop', 1), ('an', 1), ('application', 1)]
