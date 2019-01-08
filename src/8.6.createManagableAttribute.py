'''
为某个属性添加除访问和修改以外的其他处理逻辑，如合法性验证

方案：
把属性定义为property

'''

class Person:
	def __init__(self, first_name):
		self.first_name = first_name

	# getter function
	@property
	def first_name(self):
		# 这里的first_name前有个下划线
		# _first_name 是实际数据存放的地方
		return self._first_name
	
	@first_name.setter
	def first_name(self, value):
		if not isinstance(value, str):
			raise TypeError('Expected a string')
		# 这里的first_name前面多一个下划线
		self._first_name = value

	@first_name.deleter
	def first_name(self):
		raise AttributeError('Can not delete attribute')


a = Person('jiang')
print(a.first_name)
a.first_name = 'lei'
print(a.first_name)