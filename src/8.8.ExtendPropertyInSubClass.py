'''
如果子类想要扩展父类某个已经被定义为property的属性

'''

class Person:
	def __init__(self, name):
		self.name = name
		# Getter function
	
	@property
	def name(self):
	return self._name
	
	# Setter function
	@name.setter
	def name(self, value):
		if not isinstance(value, str):
			raise TypeError('Expected a string')
		self._name = value
	
	# Deleter function
	@name.deleter
	def name(self):
		raise AttributeError("Can't delete attribute")


class SubPerson(Person):
	@Person.name.getter
	def name(self):
		print('Getting name')
		return super().name

	@Person.name.setter
	def name(self, value):
		print('Setting name to', value)
		super(SubPerson, SubPerson).name.__set__(self, value)

'''
如果不知道到底哪个基类定义了property，只能通过重新定义所有property
并使用super()来将控制权传递给前面的实现
'''
