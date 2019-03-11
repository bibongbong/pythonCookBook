'''
如果有很多仅用作数据结构的类，不想写太多的__init__()函数
可以在一个基类中写一个公用的__init__()函数

当函数的参数不确定时，可以使用*args 和**kwargs，
*args 没有key值，**kwargs有key值。
这两个是python中的可变参数。*args表示任何多个无名参数，它是一个tuple；
**kwargs表示关键字参数，它是一个dict。
并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前。
例如：foo(name,age,date=newdate,birthday=date) 

'''

class Base:
	_fields = []

	def __init__(self, *args, **kwargs):
		#print(args)
		#print(kwargs)
		if len(args) > len(self._fields):
			raise TypeError('Expected {} arguments'.format(len(self._fields)))

		#if len(args)+len(kwargs) > len(self._fields):
		#	raise TypeError('Expected {} arguments'.format(len(self._fields)))

		# 赋值 args 参数
		for name, value in zip(self._fields, args):
			#print(name, value)
			setattr(self, name, value)

		# 赋值 kwargs 参数
		#for name in kwargs.keys():
		#	if name not in self._fields:
		#		raise TypeError('Invalid arguments: {}'.format(','.join(kwargs)))
		#	setattr(self, name, kwargs[name])

		#另一种实现方式
		for name in self._fields[len(args):]:
			setattr(self, name, kwargs.pop(name))
			
		#如果还有多余的参数，则报错
		if kwargs:
			raise TypeError('Invalid arguments: {}'.format(','.join(kwargs)))


class Stock(Base):
	_fields = ['name', 'shares', 'price']

	def __str__(self):
		return "name={}, shares={}, price={}".format(self.name,self.shares,self.price)

class Point(Base):
	_fields = ['x', 'y']


#s = Stock('APL', 40, 10)
#p = Point(2, 3)
#s2 = Stock('zip', 3)
s3 = Stock('zip', price=4,shares=10)
print(s3)
