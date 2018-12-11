
def spam(a, b=42):
	print(a,b)

'''
如果默认参数是一个可修改的容器，比如列表集合或者字典，可以使用None
'''
def spam1(a, b=None):
	if b is None:
		b = []

'''
默认参数的值仅仅在函数定义的时候赋值一次。一旦确定，就不能更改
'''

x = 42
def spam2(a, b=x):
	print(a,b)
spam2(1) # 1 42

x = 23
spam2(2) # 2 42

'''
默认参数的值应该是不可变对象，比如None, True, False，数字或者字符串
不能是  spam(a, b=[]),否则会影响到下一次调用这个函数时的默认值
'''

def spam3(a, b=[]):
	print(b)
	return b



