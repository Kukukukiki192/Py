# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
# 三目运算符:True_statements if expression else False_statements
a = 2
b = 3
st = "a大于b" if a > b else "a不大于b"
# 输出"a大于b"
print(st)

# 输出"a大于b"
print("a大于b") if a > b else print("a不大于b")

c = 5
d = 5
# 下面将输出c等于d
print("c大于d") if c > d else (print("c小于d") if c < d else print("c等于d"))

# True_statements可放置多条语句,支持2种执行方式:,隔开返回多条语句返回值组合成元组 ;隔开只返回第一条语句返回值
age = int(input('输入年龄:'))
s = print('年龄>=18'), "成年人" if age >= 18 else print('年龄<18')
print(s)  # (None, '成年人')
s = print('年龄>=18'); '成年人' if age >= 18 else print('年龄<18')
print(s)  # None
