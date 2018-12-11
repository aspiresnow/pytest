# -*- coding:utf-8 -*-

### 简单循环
print ("简单循环#####################################")
arr = [1,2,3,4,5]#定义一个数组
for x in arr: #循环输出 x和arr的长度
    print (x,len(arr))

### copy数组
for x in arr[:]:#在循环中修改数组时先创建一个副本
    if x>4:
        arr.insert(0,x)#在数组指定位置插入元素

### range函数
print ("range函数#####################################")
arr = range(1,10,2)#使用range函数定义一个数组,包含首不包含尾，指定步长
for x in arr:
    print (x)

### 根据下标循环数组
print ("根据下标循环数组#####################################")
strArr = ["aaa","bbb","ccc","ddd"]
for x in range(len(strArr)):
    print (x,strArr[x])

### break语句 中断循环
print ("break语句#####################################")
arr = range(1,10) #break 中断循环
for x in arr:
    if x==5:
        break;
    print (x)

### continue语句 跳过执行下一个循环
print ("continue语句#####################################")
arr = range(1, 10)  # continue语句
for x in arr:
    if x == 5:#跳过5
        continue;
    print (x)


### 循环中的else语句
print ("循环中的else语句#####################################")
for x in range(1,10):
    print (x)
    # break
else:#当（for）循环迭代完整个列表或（while）循环条件变为假，而非由break语句终止时，就会执行这个else语句
    print (x,"is a prime number") #(9, 'is a prime number')

# 使用enumerate函数输出下标和值
for i, v in enumerate(['tic', 'tac', 'toe']):
    print (i, v)

# 使用iteritems遍历字段列表，同时输出key-value
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print (k, v)

# 使用zip和format同时循环两个list，一一对应输出下标的值
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print ('What is your {0}?  It is {1}.').format(q, a)

# 使用sorted 返回一个新的排序的列表，同时保留源不变
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print (f)

# 循环内部修改正在遍历的序列（例如复制某些元素），建议您首先制作副本。在序列上循环不会隐式地创建副本
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

words

# 迭代器

s = 'abc'
it = iter(s)
while it.next:
    print (it.next())