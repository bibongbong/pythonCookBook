'''
问题：如果想得到一个由迭代器生成的切片对象，但标准切片操作并不能做到
因为它们的长度实现我们并不知道。
方案： itertools.islice() 可以用在迭代器和生成器上做切片
islice()返回一个可以生成指定元素的迭代器，它通过遍历并丢弃知道切片开始索引位置的所有元素
然后开始一个个返回元素，并直到切片结束索引位置

islice会消耗掉传入的迭代器中的数据。由于迭代器是不可逆的，所以如果需要之后再次访问这个迭代器
就要把他里面的数据放入一个列表
'''

def count(n):
	while True:
		yield n
		n+=1
c = count(0)
'''
print(c[10:20])

Traceback (most recent call last):
  File "C:\github\pythonCookBook\src\4.7.iteratorSlice.py", line 11, in <module>
    print(c[10:20])
TypeError: 'generator' object is not subscriptable
'''

import itertools

for x in itertools.islice(c, 10, 20):
	print(x)
'''
10
11
12
13
14
15
16
17
18
19
'''




