'''
问题：实现一个自定义迭代模式，跟普通的内置函数range(), reversed()不一样
方案：使用一个生成器函数来定义一个新的迭代模式
'''

def frange(start, stop, step):
	x = start
	while x < stop:
		yield x
		x += step

for n in frange(0, 4, 0.5):
	print(n)

'''
一个函数中需要一个yield语句即可转换为一个生成器。
跟普通函数不同的是，生成器只能用于迭代操作。

生成器函数的主要特征：它只会回应在迭代中使用到next操作
一旦生成器函数返回退出，迭代终止。
'''

def countdown(n):
	print('starting to count from', n)
	while n > 0:
		yield n
		n -= 1
	print('Done!')

c = countdown(3)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
'''
starting to count from 3
3
2
1
Traceback (most recent call last):
  File "C:\github\pythonCookBook\src\4.3.CreateIteratorByGenerator.py", line 31, in <module>
    print(next(c))
StopIteration
'''