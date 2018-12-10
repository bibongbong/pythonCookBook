'''
常见的IO操作如下：

with open('c:\\jiang\\python.txt') as f:
	while True:
		data = f.read(10)
		print(data)
		if data == b'':
			break

也可以用如下iter代替
iter函数，接受一个可选的callable对象和一个结尾标记作为入参
它会创建一个迭代器，这个迭代器会不断调用callable对象知道返回值和标记值相等为止

使用场景为涉及IO调用的函数，比如从套接字或文件中以数据块的方式读取数据，需要不断重复执行read()
或者recv(). 
lambda函数是为了创建一个无参数的callable对象，并未recv()或read()方法提供size参数
			
'''

with open('c:\\jiang\\python.txt') as f:
	for chunk in iter(lambda: f.read(10), ''):
		print(chunk)

'''
When each 
key is enc
ountered f
or the fir
st time, i
t is not a
lready in 
the mappin
'''		