'''
想定义某些在属性赋值上面有限制的数据结构。
所以需要自定义属性赋值函数，可以使用描述器
'''

class Descriptor:
	def __init__(self, name=None, **opts):
		print(name)
		print(opts)
		self.name = name
		for key , value in opts.items():
			setattr(self, key, value)

	def __set__(self, instance, value):
		instance.__dict__[self.name] = value


# Descriptor for enforcing types
class Typed(Descriptor):
	expected_type = type(None)

	def __set__(self, instance, value):
		if not isinstance(value, self.expected_type):
			raise TypeError('expected' + str(self.expected_type))
		super().__set__(instance, value)

# Descriptor for enforcing values
class Unsigned(Descriptor):
	def __set__(self, instance, value):
		if value < 0:
			raise ValueError('Expected >=0')
		super().__set__(instance, value)


class Integer(Typed):
	expected_type = int

class Float(Typed):
	expected_type = float

class UnsignedFloat(Float, Unsigned):
	pass

class UnsignedInteger(Integer,Unsigned):
	pass

'''
也有8.9的装饰器，来完成这个功能。更灵活更高明
'''
#Decorator for applying type checking
def Typed(expected_type, cls=None):
	print('1')
	
	if cls is None:
		print('2')
		return lambda cls: Typed(expected_type, cls)
	print('3')
	super_set = cls.__set__
	
	def __set__(self, instance, value):
		print('4')
		if not isinstance(value, expected_type):
			raise TypeError('expected ' + str(expected_type))
		super_set(self, instance, value)

	print('5')
	cls.__set__ = __set__
	return cls

# Decorator for unsigned values
def Unsigned(cls):
	super_set = cls.__set__
	
	def __set__(self, instance, value):
		if value < 0:
			raise ValueError('Expected >= 0')
		super_set(self, instance, value)

	cls.__set__ = __set__
	return cls


# Specialized descriptors
@Typed(int)
class Integer(Descriptor):
	pass

@Unsigned
class UnsignedInteger(Integer):
	pass

a = Integer(1.0)