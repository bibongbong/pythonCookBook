'''
为某个属性添加除访问和修改以外的其他处理逻辑，如合法性验证

方案：
把属性定义为property

'''

class Person:
	def __init__(self, first_name):
		#这里不是赋值，而是调用后面的setter方法first_name
		self.first_name = first_name

	# getter function
	# 是的first_name成为一个属性
	@property
	def first_name(self):
		# 这里的first_name前有个下划线
		# _first_name 是实际数据存放的地方
		return self._first_name
	
	@first_name.setter
	def first_name(self, value):
		if not isinstance(value, str):
			raise TypeError('Expected a string')
		# 这里的first_name前面多一个下划线，是实际存放数据的地方
		self._first_name = value

	@first_name.deleter
	def first_name(self):
		raise AttributeError('Can not delete attribute')


a = Person('jiang')
print(a.first_name)
a.first_name = 'lei'
print(a.first_name)

'''
三个相关联的方法名字必须一样。只有第一个first_name属性被创建后
后面两个装饰器才能被定义

一个porperty属性其实是一系列相关绑定方法的集合。
只有当确实需要对属性执行其他额外操作（比如类型检查）是才应该使用到porperty
而不是对简单的getter setter方法使用porperty，因为这样会让代码变慢

portperty还是一种定义动态计算attribute的方法，这些attribute不会被实际存储
只是在需要的时候被计算出来
'''
import math
class Circle:
	def __init__(self, radius):
		self.radius = radius

	@property
	def area(self):
		return math.pi * self.radius ** 2


c = Circle(4.0)
c.radius  4.0
c.area # Notice lack of ()  # 50.26548245743669
