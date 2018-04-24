# -*- coding:utf-8 -*-

### 列表list
list = [1,2,3,4,3]
# 末尾添加一个元素，相当于 list[len(arr):] = [5]
list.append(5)
# 将参数中的列表添加到list的末尾，即合并两个list
list.extend(range(8,9))
# 在list指定位置插入
list.insert(2,10)
# 删除list中第一个元素为2的值
list.remove(2)
# 删除list中下标为2的值，如果未指定则删除并返回最后一个元素
list.pop(2)
# 获取元素的下表
list.index(3)
# 获取元素出现的次数
list.count(3)
#反转list
list.reverse()
#计算数字list的总和
print (sum(list))
# 删除下标为2的元素，但是没有返回值
del list[2]
# 清空list
del list[:]
# 删除list变量
del list
### deque队列，先进先出，引入collections包下的deque类
from collections import deque
deque = deque(["a","b","c"])
deque.append("d")
q=deque.popleft()
print (q)

# filter函数 filter(function(x),list)
arr = filter(lambda x: x%2==0,range(1,10))
# map函数 map(function(x),list)
arr = map(lambda x: x+1,range(1,10))
# map函数可以传入多个list，下标匹配，如果不匹配 使用 None 代替
map(lambda x,y: x+y, range(1,10), range(1,10))
# 列表推导公式 等价于上面这个lambda表达式
arr = [x+1 for x in range(10)]


### 列表推导公式
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
list = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            list.append((x, y))



### 元组turples 元组在输出的时候总是有()号的，元组是不可变的
t = 12345, 54321, 'hello!'
v = ([1, 2, 3], [3, 2, 1])

### set 无序且不重复
# set = set() # 使用set()创建一个空的set集合
set = set([1,2,3,3,2,1])
print (set)
#公式推导
a = [x for x in 'abracadabra' if x not in 'abc']
print (a)

### 字典 key可以是任意不可变类型；字符串和数字常用来做key
obj = {"name":"zhangsna","age":12}
print (obj['name'])
# 输出字段的字段list
print (obj.keys())
# 删除字段属性
del obj['name']
print (obj.keys())
# dict函数从key-value创建字段
person = dict([('name', "lisi"), ('age', 12), ('sex', "男")])
print (person.keys())
# 等价
person = dict(name='lisi', age=23, sex="男")
print (person.keys())
# 字典推导
{x: x**2 for x in (2, 4, 6)}  #{2: 4, 4: 16, 6: 36}

# 序列对象可以与具有相同序列类型的其他对象相比较。比较按照 字典序 进行： 首先比较两个序列的首元素，
# 如果不同，就决定了比较的结果；如果相同，就比较后面两个元素，依此类推，直到其中一个序列穷举完。
# 如果要比较的两个元素本身就是同一类型的序列，就按字典序递归比较。如果两个序列的所有元素都相等，就认为序列相等。
# 如果一个序列是另一个序列的初始子序列，较短的序列就小于另一个。字符串的字典序按照单字符的 ASCII 顺序。
# 注意比较不同类型的对象也是合法的。比较的结果已经确定但是不一定合理： 类型按其名称进行排序。
# 因此，列表始终小于字符串，字符串总是小于元组，等等。[1] 不同数值类型按照它们的值比较，所以 0 等于 0.0，等等。
# (1, 2, 3)              < (1, 2, 4)
# [1, 2, 3]              < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)           < (1, 2, 4)
# (1, 2)                 < (1, 2, -1)
# (1, 2, 3)             == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)