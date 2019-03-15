'''
如果想定义一个接口或者抽象类，并通过执行类型检查来确保子类实现特定的方法
可以使用abc模块定义抽象基类
'''

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
	# abstractmethod 还能注解静态方法、类方法和properties
	@classmethod
	@abstractmethod
	def read(self, maxbytes=-1):
		pass

	@staticmethod
	@abstractmethod
	def write(self, data):
		pass

class SocketStream(IStream):
	def read(self, maxbytes=-1):
		pass

	def write(self, data):
		pass

#抽象类的用途：在代码中价差某类是否为特定类型、实现了特定接口
#不过Python是动态语言，过多的强制类型检查让代码变得更复杂
def serialize(obj, stream):
	if not instance(stream, IStream):
		raise TypeError('Expected an IStream')
