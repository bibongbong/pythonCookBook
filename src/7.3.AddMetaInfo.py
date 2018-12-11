'''
为函数的参数增加一些额外的信息，这样使用者就知道这个函数怎么使用
'''

def add(x:int, y:int) -> int:
	return x+y

help(add)

# add(x: int, y: int) -> int

