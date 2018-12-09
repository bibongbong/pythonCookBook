'''
问题：想在多个对象执行相同的操作，但这些对象在不同的集合中
方案：itertools.chain()，接受一个迭代器列表作为入参，返回一个迭代器。
'''
from itertools import chain
a = [1, 2, 3]
b = ['a', 'b', 'c']

for c in chain(a,b):
	print(c)

'''
当然也可以使用  for c in (a+b)
但这样会生成一个临时对象，当a和b很大时，会占用很多资源
'''

