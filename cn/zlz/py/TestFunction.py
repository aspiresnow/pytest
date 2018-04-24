# -*- coding:utf-8 -*-

### 函数 def定义一个函数,函数中的所有的赋值都是将值存储在局部符号表；而变量引用首先查找局部符号表，
# 然后是上层函数的局部符号表，然后是全局符号表，最后是内置名字表。然而，在函数内部无法给一个全局变量
# 直接赋值（除非在一个global语句中命名），虽然可以引用它们。
# 函数调用的实际参数在函数被调用时引入被调函数的局部符号表；因此，参数的传递使用传值调用（这里的值始终是对象的引用，不是对象的值）
# 保持类和函数的命名一致；通常是使用驼峰命名法命名类，使用下划线小写字母命名函数和方法 。始终使用self作为方法的第一个参数的名称
def fib(n):
    a,b=0,1 #可以通过,同时定义多个成员变量
    a, b = b, a + b
    print (a,b,n);
fib(10) #调用函数 传入参数

### 函数可以当做一个变量进行传递
f = fib
f(10)

### 定义函数参数的默认值
def fib(x,y=5,z=8):#指定了默认值的参数非必传
    print (x,y,z)
fib(2,5)
###指定参数名称调用,这样就可以跳过前面的非必传参数
fib(x=2,z=6)

### 使用None指定为空
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

### 可变参数 *names获取可变参数的列表形式，**names获取可变参数的key-value形式，*nams要在**names之前
def fib(n,*args,**names):
    print ("this is the fix arg：",n)
    for x in args:
        print ("this is the arg arr:",x)
    print ("-"*40)
    keys = sorted(names.keys())
    for k in keys:
        print (k,":",names[k])
fib("哈哈","this is the first","this is the second",third="this is the third",forth="this is the forth")

### 使用*name传递参数
arr = [2,4]
def fib(x,y):
    print ("x*y is:",x*y)
fib(*arr) ###参数传入一个数组，使用*指定分拆数组为需要的参数

### 接收对象为参数
arr = {"x":3,"y":6}
def fib(x=1,y=1):
    print ("x*y is:",x*y)
fib(**arr) ###参数传入一个对象，使用**指定分拆对象为需要的参数

### 使用lambda表达式
def fib(n):
    return lambda x: x + n
f = fib(3)
f(5)

print (fib.__doc__)