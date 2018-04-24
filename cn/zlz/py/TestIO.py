# -*- coding:utf-8 -*-
import json
### 文本格式
# str()方法、repr()方法、JSON

#如何将值转换为字符串 str()、repr()
print (str(1.0/2))
hello = 'hello, world\n'
print (repr(hello))
# str().rjust()、ljust、center返回一个新的字符串，靠左、靠右、居中显示
# x.ljust(n)[:n] 左补齐n位并截取n个长度
print (str("abcdefg").rjust(3)[:3])
# str.zfill() 补0
print (str("abcdefg").zfill(10))
# 使用format格式输出，支持按照下标和字典匹配输出
print ('The story of {0}, {1}}.'.format('Bill', 'Manfred'))

# dumps 将一个对象转换成json
print (json.dumps([1, 'simple', 'list']))
# dump函数直接将对象json化后存到文件
json.dump({"a":1,"b":2}, open('workfile1', 'w'))
# load函数从文件中读出一个对象
print (json.load(open('workfile1', 'r')))


### 读写文件 open(fileName,mode)  w：写入、r：读取 、rb：读取二进制 、wb：写入二进制

# 在当前目录写一个workfile文件
f = open('workfile', 'w')
f.write("this is the first line\n")
f.write("this is the second line\n")
f.write("this is the third line\n")
# 使用完文件后关闭
f.close()
# print f

f=open('workfile','r')
print (f.readline())
print (f.readline())
print (f.readline())
# 使用完文件后关闭
f.close()

# 循环读取文件，如果开启的文件已被读完，输出空
f=open('workfile','r')
for line in f:
        print (line),
# 使用完文件后关闭
f.close()

# 读取所有行
f=open('workfile','r')
print (f.readlines())
# 使用完文件后关闭
f.close()

#读取所有行
f=open('workfile','r')
print (list(f))
# 使用完文件后关闭
f.close()

# 使用with 在文件使用完之后会自动关闭，即使出现异常，类似finally里面关闭流
with open('workfile', 'r') as f:
    read_data = f.read()
f.closed

# 代表文件对象在文件中的指针位置，该数值计量了自文件开头到指针处的字节数
f=open('workfile','r')
print (f.tell())

# f.seek(offset, from_what)。新的位置由参考点加上 offset 计算得来，参考点的选择则来自于 from_what 参数。from_what 0：以文件的开始为参考点，1：以当前的文件位置为参考点，2：以文件的结尾为参考点
f.seek(2, 0)
print (f.tell())
