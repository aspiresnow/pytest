# -*- coding:utf-8 -*-

# 类继承机制允许有多个基类，继承的类可以覆盖其基类或类的任何方法，方法能够以相同的名称调用基类中的方法。
# 对象可以包含任意数量和种类的数据。和模块一样，类同样具有 Python 的动态性质：它们在运行时创建，并可以在创建之后进一步修改。

from socket import gethostname

from .. TestFunction import fib

print fib(1)
print gethostname()
print 'test_class'