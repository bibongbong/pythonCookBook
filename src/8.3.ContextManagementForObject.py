'''
问题：如果想让对象支持上下文管理协议（with语句）
方案：需要实现__enter__()和__exit__()
'''

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
	def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
		self.address = address
		self.family = family
		self.type = type
		self.sock = None
	def __enter__(self):
		if self.sock is not None:
			raise RuntimeError('Already connected')
		self.sock = socket(self.family, self.type)
		self.sock.connect(self.address)
		return self.sock
	def __exit__(self, exc_type, exc_val, tb):
		self.sock.close()
		self.sock = None

'''
这个类表示一个网络连接，初始化时不做任何事情。连接的简历和关闭使用with语句自动完成
'''
from functools import partial

conn = LazyConnection(('www.python.org', 80))

with conn as s:
	s.send(b'GET /inde.html HTTP/1.0\r\n')
	s.send(b'Host: www.python.org\r\n')
	s.send(b'\r\n')
	resp = b''.join(iter(partial(s.recv, 8192), b''))

'''
当出现with语句，对象的__enter__()方法会触发，它的返回值（如果有的话）会被赋值给as
声明的变量。然后with语句里面的代码开始执行。最后__exit__()方法被触发进行清理工作
不管with中发生什么，就算代码发生异常，控制流也会执行完。
__exit__()方法能自己决定怎么利用这个异常信息，或者忽略它

在需要管理一些资源比如文件、网络连接和锁的编程环境中，使用上下文管理器是很普遍的。
这样可以在任何情况下都能最后被释放掉。
'''