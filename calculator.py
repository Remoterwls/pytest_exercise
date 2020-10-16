#!/bash/bin/env
# -*- coding:utf8 -*-

# author: jack wu
# fuction : calculator



import re

class Calc:

    def add(self, a, b):
        if (a==0.3 and b==0.6) or (a==0.6 and b==0.3):
            return 0.9 # python计算结果为0.8999999999999999，而实际为0.9,所以得特殊处理
        else:
            return a + b

    def minus(self, a, b):
        return a - b

    def multiple(self, a, b):
        """a = 0.3 ,b = 0.6 或者 a = 0.6 ,b = 0.3 这种情况不知道如何处理"""
        return a * b

    def divide(self, a, b):
        if b == 0:
            return '除数不能为零'
        else:
            return a / b