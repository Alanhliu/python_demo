#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-14 16:43:38
# @Author  : liuhao (liuhao257@163.com)
# @Link    : http://example.org
# @Version : $Id$

import os

def sum(x,y):
	return x+y

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
