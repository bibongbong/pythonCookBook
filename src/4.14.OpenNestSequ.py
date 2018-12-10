'''
问题：将一个多层嵌套的序列展开成一个单层列表
方案：yield from
'''
from collections import Iterable

items = [1, 2, [3, 4, [5, 6], 7], 8]
items1 = ['Dave', 'Paula', ['Thomas', 'Lewis']]

# ignore_types=(str, bytes) 是为了防止过度展开成单个字符
def openNestSeq(items, ignore_types=(str, bytes)):
	for item in items:
		if isinstance(item, Iterable) and not isinstance(item, ignore_types):
			yield from openNestSeq(item)
		else:
			yield item



for i in openNestSeq(items):
	print(i)

for i in openNestSeq(items1):
	print(i)