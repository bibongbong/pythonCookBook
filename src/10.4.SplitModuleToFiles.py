'''
程序模块可以通过变成包来分割成多个独立的文件
'''
# mymodule.py
class A:
	pass

class B:
	pass

'''
如果想把这个文件分成两个文件，每个文件定义一个类。
先用mymodule目录来替换mymodule.py，并创建一下文件
mymodule/
	__init__.py
	a.py
	b.py
'''
# a.py
class A:
	def spam(self):
		print('A.spam')


# b.py
from .a import A
class B(A):
	def bar(self):
		print('B.bar')

'''
最后在__init__.py中将2个文件粘合
'''

# __init__.py
from .a import A
from .b import B


