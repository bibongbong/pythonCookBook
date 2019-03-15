'''
将某个实例的属性访问代理到内部另一个实例中去
三种方式：
'''

class A:
	def spam(self, x):
		pass
	def foo(self):
		pass

class B:
	def __init__(self):
		self._a = A()
	def spam(self, x):
		self._a.spam(x)
	def foo(self):
		self._a.foo()

# 如果有大量的属性需要代理，可以使用__getattr__()
class B2:
	def __init__(self):
		self._a = A()

	#这个方法在访问attribute不存在时会被调用
	def __getattr__(self, name):
		return getattr(self._a, name)