'''
创建一个实例时，如何绕过__init__()
可以通过__new__(),创建一个未初始化的实例
'''

class Date:
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

d = Date.__new__(Date)
print(d.__dict__) # {}
data = {'year':2012, 'month':8, 'day':28}
for key, value in data.items():
	setattr(d, key, value)

print(d.__dict__) # {'year': 2012, 'month': 8, 'day': 28}