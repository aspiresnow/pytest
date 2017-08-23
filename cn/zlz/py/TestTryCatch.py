# -*- coding:utf-8 -*-

# try:
# except ***Error:   -----except (RuntimeError, TypeError, NameError): 多个异常使用()括起来
# 最后一个except 可以省略异常名称

import sys
# try:
#     f = open('workfile')
#     s = f.readline()
#     i = int(s.strip())
# except IOError as e:
#     print "I/O error({0}): {1}".format(e.errno, e.strerror)
# except ValueError:
#     print "Could not convert data to an integer."
# except:
#     print "Unexpected error:", sys.exc_info()[0]
#     raise #将异常抛出
# finally: 最终执行
# try...except语句有一个可选的else 子句，else 必须放在所有 except 子句的后面。try 语句没有抛出异常时执行 else 子句
for arg in sys.argv[0:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()

# 异常实例绑定了_ _str__()，因此异常的参数可以直接打印而不必引用.args
try:
    raise Exception("a","b")
except Exception as inst:
    print type(inst)
    print inst.args
    print inst # __str__()
    x,y = inst.args
    print 'x = ', x
    print 'y = ',y
finally:
    print 'finally' # 最终会执行

# 创建自定义异常继承Exception
class MyError(Exception):
    def __init__(self, value): #覆盖 __init__ 方法
        self.value = value
        def __str__(self):  # 覆盖 __str__ 方法
            return repr(self.value)