'''
问题：如果你希望函数的某些参数强制使用关键字参数传递
方案：将强制关键字参数放到某个*或者单个*后面
'''

def recv(maxsize, *, block,size):
	pass

# TypeError: recv() takes 1 positional argument but 2 were given
#recv(1000, True) # TypeError
recv(1000, block=True,size=10)	#OK

'''
很多时候，使用强制关键字参数会比使用位置参数更加清晰，程序更加有可读性
上面的第一个，可能不清楚True参数到底干嘛用的
而第二个清楚的表明，是针对block属性的

另外使用强制关键字参数也会比使用**kwargs参数更好，因为使用函数help时的输出更容易理解

'''
help(recv)
'''
Help on function recv in module __main__:

recv(maxsize, *, block, size)
'''