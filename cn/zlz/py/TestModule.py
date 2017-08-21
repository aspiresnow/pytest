# -*- coding:utf-8 -*-

### python模块

# 使用import引入一个python模块，即python文件的名字，使用该名字调用模块中的方法
import HelloWorld

HelloWorld.run("lizhi")
# __name__ 全局变量获取python的模块名
# if __name__ == "__main__": 当模块名是 __main__ 时作为python脚本的入口

# dir列出模块中的所有变量
dir(HelloWorld)

s = 1
dir()

### __init__.py 文件声明这个是个包，可以编辑指定__all__ = ["echo", "surround", "reverse"]控制import *会引入哪些