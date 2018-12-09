'''
问题：同时迭代多个序列，每次分别从一个序列取一个元素
方案：zip() 
zip(seq1, seq2)会生成一个可返回元组(x,y)的迭代器，x来自seq1， y来自seq2
一旦其中某个序列到达尾部，迭代结束
'''

a = [1, 2, 3]
b = ['a', 'b', 'c', 'd']
for x,y in zip(a,b):
	print(x,y)
'''
1 a
2 b
3 c
'''

'''
如果想遍历完长的再结束，可以使用zip_longest()来代替
这个功能也可以使用pandas的merge的外连接来实现
'''
from itertools import zip_longest
for x,y in zip_longest(a,b):
	print(x,y)
'''
1 a
2 b
3 c
None d
'''

'''
zip()返回的是迭代器，如果需要将结对的值存储在列表，则要使用list函数
'''

print(list(zip(a,b)))
# [(1, 'a'), (2, 'b'), (3, 'c')]




