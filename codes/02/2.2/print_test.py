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
# 默认值:            空格隔开   输出换行   屏幕输出(import sys)控制输出缓存(保持False获得较好性能)
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

user_name = 'Charlie'
user_age = 8
# 同时输出多个变量和字符串
print("读者名:" , user_name, "年龄:", user_age)
# 同时输出多个变量和字符串，指定分隔符
print("读者名:" , user_name, "年龄:", user_age, sep='|')
# 指定end参数，指定输出之后不再换行
print(40, '\t', end="")
print(50, '\t', end="")
print(60, '\t', end="")
f = open("poem.txt", "w") # 打开文件以便写入(w)
print('沧海月明珠有泪', file=f)
print('蓝田日暖玉生烟', file=f)
f.close()
