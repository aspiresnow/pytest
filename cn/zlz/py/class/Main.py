# -*- coding:utf-8 -*-

from Module import person,moduleName,fib

print (moduleName)

fib("fib")

# 创建p1对象

# print person.__category #无法获取私有属性
print (person.getCategory())
# print person.run() #无法通过类对象调用实例对象方法
print (person.name)
p1 = person("张三","男") # 传入参数创建对象
print (p1.name) #创建实例对象后，通过实例对象可以获取到name属性的值
print (person.name) # 创建实例对象后，类对象无法获取到name属性
p1.speak() # 实例对象可以调用类方法
p1.makeEge() # 实例对象可以对象方法
print (person.watch())




# 创建p2对象
p2= person("小红","女")
print (p2.name)
p2.name = "晓红"
print (p2.name)
print (p1.name)
# print p1.__privateFunc # 在外部无法访问私有方法
# print person.__privateCls