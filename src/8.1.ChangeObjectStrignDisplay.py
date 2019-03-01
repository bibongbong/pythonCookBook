'''
如果想要对象实例的打印显示更具有可读性，可以重新定义它的__str()__和__repr()__方法
'''

class Pair:
	def __init__(self, x, y):
		self.x = x
		self.y = y 
	def __repr__(self):
		return 'Pair({0.x!r}, {0.y!r})'.format(self)
	def __str__(self):
		return 'Pair({0.x!s}, {0.y!s})'.format(self)

'''
repr方法返回一个实例的代码表示,str方法将实例转换为一个字符串	
如果__str__()没有被定义，name就会使用__repr()__来代替输出
0.x对应的是第一个参数的x属性，0实际指的就是self本身
'''
