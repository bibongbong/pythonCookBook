
'''
lambda中的x是一个自由变量，是在运行时绑定，不是在定义时绑定，这个跟函数的默认值参数定义不同
所以在调用a(10)时，lambda里的x是20
'''
x = 10
a = lambda y: x+y
x = 20
b = lambda y: x+y

print(a(10))	#30
print(b(10))	#30

'''
如果想让某个匿名函数在定义时就捕获，可以将这个参数值定义成默认参数即可
'''
x = 10
a = lambda y, x=x: x+y
x = 20
b = lambda y, x=x: x+y

print(a(10)) # 20
print(b(10)) # 30








