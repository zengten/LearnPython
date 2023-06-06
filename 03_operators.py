print(3 > 2)
print(3 != 2)
print('True == False: ', True == False)

# SyntaxWarning: "is" with a literal. Did you mean "=="?
print('1 is 1: ', 1 is 1)
# SyntaxWarning: "is not" with a literal. Did you mean "!="?
print('a is a: ', 'a' is not 'a')
print('e in hello: ', 'e' in 'hello')

# *号也能表示次数
print('哈哈' * 4)

# 逻辑运算符
print(3 > 2 and 5 >= 1)
print(3 > 2 or 5 < 1)
print(not 3 > 2 and 5 > 1)
print(not not True)
