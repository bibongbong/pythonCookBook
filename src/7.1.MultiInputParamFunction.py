'''
要让函数接受任意数量的位置参数，可以使用*
如下，rest室友所有其他参数组成的元组
'''

def avg(first , *rest):
	#print((first + sum(rest))/(1+len(rest)))
	for i in rest:
		print(i)

avg(2,4,5,7)

'''
为了接受任意数量的关键字参数，可以使用**开头的参数
'''
import html

def make_element(name, value, **attrs):
	print(attrs)
	keyvals = [' %s="%s"' % item for item in attrs.items()]
	attr_str = ''.join(keyvals)
	element = '<{name}{attrs}>{value}</{name}>'.format(
				name=name,
				attrs=attr_str,
				value=value)
	return element

print(make_element('item', 'Albatross', size='large', quantity=6))
'''
<item size="large" quantity="6">Albatross</item>

这里attrs是一个包含所有被传入进来的关键字参数的字典
也可以同时接受任意数量的位置参数和任意数量的关键字参数，同时使用*和**
'''

def anyargs(*args, **kwargs):
	print(args)
	print(kwargs)

anyargs('a', 1, 1.02, size='largre', quantity=7)
'''
('a', 1, 1.02)
{'size': 'largre', 'quantity': 7}
'''

'''
*参数只能出现在函数定义中最后一个位置参数前面，而**只能出现在最后一个参数。
*参数后面任然可以定义其他参数
'''
def a(x, *args, y):
	pass

def b(x, *args, y, **kwargs):
	pass

	




