# -*- coding:utf-8 -*-

import re
#match方法严格去匹配模式
m = re.match('foo','food is a food')
if m is not None :
   print (m.group())

#search方法从左往右找到第一个出现的位置
m = re.search('foo','a food is a food')
if m is not None :
    print m.group()