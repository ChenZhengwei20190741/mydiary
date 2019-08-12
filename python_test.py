#!/usr/bin/env python
# coding=utf-8

# name = raw_input('nihao:')
# print 'hello world!', name

# list = ['zchemisddddddtry', 'physics', 1979, 2000]
# del list[2]
# print "hello", list

# list1 = []
# list1.append('google')
# print list1
# print len([0, 1, 2])
# for x in list:
#     print x
# print cmp(list, list1)
# tup1 = ('hello', 'world')
# list.extend(tup1)
# print list

# list.reverse()
# print list
# dict = {
#     'Name': 'Zara', "Age": 7, 'class': "firest"
# }

# print dict.values()
import calendar
import time

tick = time.localtime(time.time())
localtime = time.asctime(tick)
print localtime


cal = calendar.month(2019, 8)
print "以下输出2019年8月份日历：\n", cal
