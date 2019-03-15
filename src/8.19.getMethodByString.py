'''
如果有一个字符串形式的方法名，想通过他调用某对象的方法
可以通过getattr来取得方法
'''

class A:
	def foo(self, value):
		print('foo %s',value)

a = A()
# getattr是查找属性，然后以函数的方式调用它
getattr(a, "foo")(3)

import operator
# methodcaller 是创建一个可调用对象，并提供所有参数，
# 调用的时候将实例对象传递给它
operator.methodcaller('foo', 4)(a)