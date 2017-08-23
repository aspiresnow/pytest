# -*- coding:utf-8 -*-

# 属性
moduleName = "module"

# 函数
def fib(x):
    print x

# 类
class person:


    # 属性没有被类方法引用时不区分类属性和对象属性，同名时对象属性会覆盖类属性
    # 类方法中引用某个属性，该属性必定是类属性
    # 私有属性
    __category = 'human'
    # 公有属性
    name = ''
    # 公有属性
    sex = ''

    # 构造方法，创建对象时调用
    def __init__(self, name, sex):
        print "执行构造方法:",name,sex
        self.name = name

    # 析构方法，释放对象时调用
    def __del__(self):
        pass
        # print "执行析构方法:"

    # 获取实例对象私有属性
    def getCategory(self):
        return self.__category

    # 获取类对象私有属性
    @classmethod
    def getCategory(cls):
        return cls.__category

    # 实例对象方法，通过对象调用
    def makeEge(self): #做鸡蛋
        print self.name, '会做鸡蛋'
        self.__privateFunc() #实例对象私有方法只能在类内部调用

    # 类对象方法，可以通过类和对象调用
    @classmethod
    def speak(cls):
        print "person can speak!"
        cls.__privateCls() #类对象私有方法只能在类内部调用

    # 静态方法，引用什么属性用相应的 cls 和 self
    @staticmethod
    def watch():
        return "person can watch!"

    # 私有类对象方法
    @classmethod
    def __privateCls(cls):
        print "private cls function"

    # 实例对象私有方法
    def __privateFunc(self):
        print "private function"