'''
问题：反向迭代
方案：使用内置的reversed()函数
'''

a = [1, 2, 3, 4]
for i in reversed(a):
	print(i)

'''
反向迭代仅仅当对象的大小可以预先确定，或者对象实现了__reversed__()
特殊方法时才能生效。如果两者都不符合，那必须先将对象转换成一个列表
但如果可迭代对象元素很多的话，预先转换成一个list会消耗大量内存
'''

f = open('2.1.StringSplit.py', encoding='UTF-8')
for line in reversed(list(f)):
	print(line, end='')


'''
如何在自定义类上，实现__reversed__()来实现反向迭代
'''

class CountDown:
	def __init__(self, start):
		self.start = start

	# 正向迭代
	def __iter__(self):
		n = self.start
		while n > 0:
			yield n
			n -= 1

	# reverse iterator
	def __reversed__(self):
		n = 1
		while n <= self.start:
			yield n
			n+=1

for rr in reversed(CountDown(30)):
	print(rr)

for rr in CountDown(30):
	print(rr)


class MyList:
	def __init__(self, start, end, step=0.1):
		self.start = start
		self.end = end
		self.step = step

	# 正向迭代
	def __iter__(self):
		i = self.start
		while i < self.end:
			yield i
			i+=self.step

	# 反向迭代
	def __reversed__(self):
		i = self.end
		while i > self.start:
			yield i
			i-=self.step

mylist = MyList(1, 10, 0.5)


for i in reversed(mylist):
	print(i)

for i in mylist:
	print(i)

