'''
如果想将一个属性定义成一个property，并只在访问时才会计算结果。
一旦被访问过，结果值就会被缓存起来。

定义一个迟疑数据的方法就是描述符类。
'''

class lazyproperty:
	def __init__(self, func): # 注意这里传入的是func
		self.func = func
	def __get__(self, instance, cls):
		print(instance)
		print(cls)
		if instance is None:
			print("lazyproperty if")
			return self
		else:
			# 调用Circle.area()计算出area的值
			value = self.func(instance)
			# self.func.__name__ 就是area, 
			# setattr的作用就是把area的值存到instance.__dict__中
			# setattr(object, attrName, value)
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



'''
lazyproperty 类利用这一点，使用__get__() 方法在实例中存储计算出来的值，
这个实例使用相同的名字作为它的property。这样一来，结果值被存储在实例字典中并
且以后就不需要再去计算这个property 了。
'''
c = Circle(4)
print(c.__dict__)	# {'radius': 4}
print(c.area)		# 50.26548245743669
print(c.__dict__) 	# {'radius': 4, 'area': 50.26548245743669}
print(c.area)		# 50.26548245743669


