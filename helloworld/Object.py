#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-15 14:29:46
# @Author  : liuhao (liuhao257@163.com)
# @Link    : http://example.org
# @Version : $Id$

import os

# class Student(object):
#     pass

# bart = Student()

# print(bart)
# print(Student)


# class Student(object):

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))

#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'

# bart = Student('Bart Simpson', 59)

# print(bart.name)
# 因为python中print函数需要返回值，如果你在print函数中所放的函数没有返回值，那么print将会return None
# print(bart.print_score())
# print(bart.get_grade())

# class Student(object):

#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score

#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))

#     def get_name(self):
#         return self.__name

#     def get_score(self):
#         return self.__score

#     def set_name(self, name):
#         self.__name = name    

#     def set_score(self, score):
#         self.__score = score

# bart = Student('Bart Simpson', 59)

# print(bart.__name)
# print(bart.get_name())
# bart.set_name("liuhao")
# print(bart.get_name())
# print(bart._Student__name)


# 继承和多态
# class Animal(object):
#     def run(self):
#         print('Animal is running...')

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# dog = Dog()
# dog.run()

# cat = Cat()
# cat.run()


# class Student(object):
#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self, value):
#         self._birth = value

#     @property
#     def age(self):
#         return 2018 - self._birth
#     # @age.setter
#     # def age(self, value):
#    	# 	self._age = value

# s = Student()
# s.birth = 1991

# print(s.birth)
# s.age = 30
# print(s.age)