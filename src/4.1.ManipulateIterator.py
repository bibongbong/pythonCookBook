'''
迭代器是Python最强大的功能，它不仅是处理序列元素的一种方法

想要遍历一个科迭代对象中的所有元素，但是不用for循环
手动遍历可迭代对象，使用next函数，并在代码中捕获StopIteration异常
'''

def manual_iter():
	with open('2.1.StringSplit.py', encoding='UTF-8') as f:
		try:
			while True:
				line = next(f)
				print(line, end='')
		except StopIteration:
			print("catch StopIteration")
			pass

#manual_iter()

'''
也可以不通过捕获异常，而是返回一个指定值来标记结尾
'''

def manual_iter_NotCatchException():
	with open('2.1.StringSplit.py', encoding='UTF-8') as f:
		while True:
			line = next(f, None)
			if line is None:
				break
			print(line, end='')

#manual_iter_NotCatchException()


'''
底层迭代的机制
'''
items = [1,2,3]
it = iter(items)
print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3
print(next(it))
'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration
'''

