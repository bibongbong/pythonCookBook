'''
如果想将一个属性定义成一个property，并只在访问时才会计算结果。
一旦被访问过，结果值就会被缓存起来。

定义一个迟疑数据的方法就是描述符类。
'''

class lazyproperty:
	def __init__(self, func):
		self.func = func
	def __get__(self, instance, cls):
		if instance is None:
			print("lazyproperty if")
			return self
		else:
			print("lazyproperty else")
			value = self.func(instance)
			setattr(instance, self.func.__name__, value)
			return value

import math

class Circle:
	def __init__(self, radius):
		self.radius = radius

	@lazyproperty
	def area(self):
		print('Computing area')
		return math.pi * self.radius **2

	@lazyproperty
	def perimeter(self):
		print('Computing perimeter')
		return 2*math.pi*self.radius


c = Circle(4.0)
print(c.area)
print(c.area)
print(c.perimeter)
print(c.perimeter)