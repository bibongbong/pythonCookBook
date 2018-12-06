'''
问题：当构建一个自定义容器对象，里面包含列表、元组或其他可迭代对象。你想直接在你的心容器对象上执行迭代操作
方案：你只需定义一个 __iter__()方法，将迭代操作代理带容器内部的对象上

Python的迭代器协议需要__iter__()返回一个实现了__next__()方法的迭代器对象。
这里的iter()函数使用了简化的代码，iter(s)只是简单的调用s.__iter__()来返回对应的迭代器对象
就像len(s)会调用s.__len__()
'''

class Node:
	def __init__(self, value):
		self._value = value
		self._children = []

	def __repr__(self):
		# !r 是str.format的格式处理方式，表示在参数上调用repr()
		# !s 在参数值上调用str()
		return 'Node({!r})'.format(self._value)

	def add_child(self, node):
		self._children.append(node)

	def __iter__(self):
		return iter(self._children)

	def __eq__(self,node):
		return (self._value == node._value)


if __name__ == '__main__':
	root = Node(0)
	child1 = Node(1)
	child2 = Node(2)
	root.add_child(child1)
	root.add_child(child2)


	for ch in root:
		#  如果没有实现__iter__()，会报错： TypeError: 'Node' object is not iterable
		print(ch)

'''
Node(1)
Node(2)
'''




