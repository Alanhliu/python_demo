#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-14 11:00:48
# @Author  : liuhao (liuhao257@163.com)
# @Link    : http://example.org
# @Version : $Id$

import os
# print('I\'m ok')
# print(r'\\\t\\')

# print(True and True)
# print(True and False)
# print(True or True)
# print(True or False)

# print(not True)
# print(not False)
# print(not 1 > 2)

# age = 19
# if age >= 18:
#     print('adult')
# else:
#     print('teenager')

# int a = 123
# a = 123
# a = "ABC"
# print(a);

# classmates = ['Michael', 'Bob', 'Tracy']
# print(len(classmates))
# print(classmates[0])
# print(classmates[-1])
# classmates.append('liuhao')
# print(classmates)
# classmates.pop()
# classmates.pop(1)
# classmates.pop(-3)
# print(classmates)
# classmates[1] = 'Sarah'
# print(classmates)

# t = (1, 2)
# print(t)

# import a

# print(a.sum(2,3));

# print(a.fact(5));


# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# # 前闭后开
# print(L[:3])
# print(L[1:3])

# L = list(range(100))
# print(L);
# print(L[:10])
# print(L[-10:])
# print(L[10:20])
# print(L[:10:2])

# str = 'ABCDEFG'
# print(str[:3])

# d = {'a': 1, 'b': 2, 'c': 3}

# for key in d:
# 	print(key)
# 	print(d[key])

# for ch in 'ABC':
# 	print(ch)

# print(list(range(1, 11)))

# L = []
# for x in range(1, 11):
# 	L.append(x * x)
# print(L)

# print([x * x for x in range(1, 11)])
# print([x * x for x in range(1, 11) if x % 2 == 0])
# print([m + n for m in 'ABC' for n in 'XYZ'])
# print([d for d in os.listdir('.')])
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for k, v in d.items():
# 	print(k, '=', v)

# from collections import Iterable
# print(isinstance([], Iterable))
# print(isinstance((), Iterable))
# print(isinstance('abc', Iterable))
# print(isinstance((x for x in range(10)), Iterable))
# print(isinstance(100, Iterable))

# for x in [1, 2, 3, 4, 5]:
#     pass
#     print(x)

# 首先获得Iterator对象:
# it = iter([1, 2, 3, 4, 5])
# # 循环:
# while True:
#     try:
#         # 获得下一个值:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         break


# def f(x):
# 	return x * x

# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# r = map(f, L)
# print(list(r))

# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

from functools import reduce
# def add(x, y):
# 	return x + y
# r = reduce(add, [1, 3, 5, 7, 9])
# print(r)

# def fn(x, y):
# 	return x * 10 + y
# r = reduce(fn, [1, 3, 5, 7, 9])
# print(r)

# def fn(x, y):
# 	return x * 10 + y
# def char2num(s):
# 	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# 	return digits[s]
# r = reduce(fn, map(char2num, '13579'))
# print(r)


# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))

# print(type("123"))
# print(type(str2int("123")))


# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def char2num(s):
#     return DIGITS[s]

# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# print(type("123"))
# print(type(str2int("123")))


# print(type(int("123")))
# print(type(str(123)))
# print(hex(18))
# print(int('FA', 16))

# def is_odd(n):
#     return n % 2 == 1

# l = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# print(l)

# print(sorted([36, 5, -12, 9, -21]))
# print(sorted([36, 5, -12, 9, -21], reverse=True))
# print(sorted([36, 5, -12, 9, -21], key=abs))


# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax
# f = calc_sum(1, 3, 5, 7, 9)
# print(f)

# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum

# f = lazy_sum(1, 3, 5, 7, 9)
# print(f)
# print(f())
# f1 = lazy_sum(1, 3, 5, 7, 9)
# f2 = lazy_sum(1, 3, 5, 7, 9)
# print(f1==f2)


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs

# f1, f2, f3 = count()
# print(f1(),f2(),f3())

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs

# f1, f2, f3 = count()
# print(f1(),f2(),f3())


# def f(x):
#     return x * x
# print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def now():
	print('2015-3-25')
f = now

print(now.__name__)
print(f.__name__)

