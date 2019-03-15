'''
使用类方法来实现多个构造器
'''

import time

class Date:
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

	@classmethod
	def today(cls):
		t = time.localtime()
		return cls(t.tm_year, t.tm_mon, t.tm_mday)

a = Date(2021, 2, 2)
b = Date.today()
print(b)