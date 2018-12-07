'''
问题：你想迭代遍历一个集合中元素的所有可能的排列组合
方案：itertools模块提供了三个函数
permutations(),接受一个集合并产生一个元组女咧，每个元组有集合中所有元素的一个可能排列组成。
也就是打乱集合中元素排列顺序生成的一个元组
'''

items = ['a', 'b', 'c']
from itertools import permutations

for p in permutations(items):
	print(p)

'''
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
'''

# 如果要指定长度的所有排列，可以传递一个可选的长度参数
for p in permutations(items, 2):
	print(p)
'''
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'c')
('c', 'a')
('c', 'b')
'''

# 使用itertools.combinations()可得到输入集合中元素的所有组合，这里是组合不是排列，组合部分先后顺序
from itertools import combinations
for p in combinations(items, 3):
	print(p) # ('a', 'b', 'c')

for p in combinations(items, 2):
	print(p)
'''
('a', 'b')
('a', 'c')
('b', 'c')
'''

for p in combinations(items, 1):
	print(p)
'''
('a',)
('b',)
('c',)
'''

'''
combinations()，元素被选取就会被从候选中剔除
而combinations_with_replacement()允许同一个元素多次被选择
'''
from itertools import combinations_with_replacement
for p in combinations_with_replacement(items, 3):
	print(p)
'''
('a', 'a', 'a')
('a', 'a', 'b')
('a', 'a', 'c')
('a', 'b', 'b')
('a', 'b', 'c')
('a', 'c', 'c')
('b', 'b', 'b')
('b', 'b', 'c')
('b', 'c', 'c')
('c', 'c', 'c')
'''

