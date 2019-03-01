'''
使用super()函数，调用父类的方法
常被用在__init__()中用来确保父类被正确的初始化
'''
class A:
	def spam(self):
		print('A.spam')

class B(A):
	def spam(self):
		print('B.spam')
		super().spam() # Call parent spam()


'''
有时会用Base.__init__()的方式调用父类的方法
但在多继承的时候就会出现问题
'''
class Base:
	def __init__(self):
		print('Base.__init__')

class A(Base):
	def __init__(self):
		Base.__init__(self)
		print('A.__init__')

class B(Base):
	def __init__(self):
		Base.__init__(self)
		print('B.__init__')

class C(A,B):
	def __init__(self):
		A.__init__(self)
		B.__init__(self)
		print('C.__init__')

c = C()
'''
Base.__init__	# Base.__init__ 被两次调用
A.__init__
Base.__init__
B.__init__
C.__init__

把Base.__init__换成 super().__init__，就只会被调用一次
'''
