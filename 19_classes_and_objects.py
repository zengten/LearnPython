# 定义class
class Person:
    def __init__(self):
        self.nickname = 'ZhangSan'

    # 这个方法在对象销毁时才调用
    def __del__(self):
        print(f'{self.nickname} exec del')

    # str方法一般用于打印对象信息，必须返回一个字符串
    def __str__(self):
        return 'nickname=' + self.nickname


# 实例化对象
person = Person()
print(person)  # 输出对象在内存中的地址 <__main__.Person object at 0x0000021945829CA0>
print(person.nickname)  # ZhangSan
print(person.__str__())  # nickname=ZhangSan


class User:
    # 构造器指定默认值，相当于多种构造期
    def __init__(self, nickname='', age=0, gender='保密'):
        self.nickname = nickname
        self.age = age
        self.gender = gender
        self.skills = []

    # 默认方法是实例方法,也可以指定@classmethod表示实例方法
    def user_info(self):
        print(f'nickname={self.nickname},age={self.age},gender={self.gender},skills={self.skills}')

    # 表示静态方法
    @staticmethod
    def say_hello(args1, args2):
        print(f'hello static method, args1={args1}, args2={args2}')

    def add_skill(self, args):
        self.skills.append(args)


User.say_hello('hello', 'world')  # hello static method, args1=hello, args2=world
user = User()
user.user_info()  # nickname=,age=0,gender=保密
user.add_skill('Java')
user.add_skill('Python')
user.user_info()  # nickname=,age=0,gender=保密,skills=['Java', 'Python']


# 继承
class Animal:  # 动物父类
    def __init__(self, name):
        self.name = name

    def make_sounds(self):
        pass


class Dog(Animal):  # 狗继承动物
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def make_sounds(self):
        print(f'{self.name},age={self.age} 汪汪汪~')


class Cat(Animal):  # 狗继承动物
    def __init__(self, name, gender):
        self.gender = gender
        super().__init__(name)

    def make_sounds(self):
        print(f'{self.name},gender={self.gender} 喵喵喵~')


dog = Dog('小七', 22)
dog.make_sounds()  # 小七,age=22 汪汪汪~
cat = Cat('苗苗', '男')
cat.make_sounds()  # 苗苗,gender=男 喵喵喵~
