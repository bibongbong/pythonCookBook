'''
如果想通过format()函数和字符串方法使得一个对象能支持自定义的格式化
你可以在类上面定义__format()__
'''

_formats = {'ymd' : '{d.year}-{d.month}-{d.day}',
	'mdy' : '{d.month}/{d.day}/{d.year}',
	'dmy' : '{d.day}/{d.month}/{d.year}'}

class Date:
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = 	day

	def __format__(self, code):
		if code == '':
			code = 'ymd'
		fmt = _formats[code]
		return fmt.format(d=self)

d = Date(2012, 12, 21)
print(format(d)) # 2012-12-21
print(format(d, 'mdy'))	# 12/21/2012

'''
格式化代码的解析工作完全由类自己决定，__format__()给字符串格式化功能提供了钩子，