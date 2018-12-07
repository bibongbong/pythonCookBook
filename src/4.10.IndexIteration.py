'''
问题：在迭代一个序列的同时跟踪正在被处理的元素索引
方案：内置 enumerate()
'''

mylist = ['a', 'b', 'c']
for index, item in enumerate(mylist):
	print(index, item)
'''
0 a
1 b
2 c
'''

# 如果要按传统行号(从1开始)输出，可以传递一个参数
from collections import defaultdict

with open('1.16.filterSequence.py', encoding='UTF-8') as f:
	for lineNo, line in enumerate(f, 1):
		#print(lineNo, line)
		pass

# 如果想将一个文件中出现的单词映射到它出现的行号上
words_summary = defaultdict(list)
with open('1.16.filterSequence.py', encoding='UTF-8') as f:
	for lineNo, line in enumerate(f, 1):
		words = [w.strip().lower() for w in line.split()]

		for word in words:
			words_summary[word].append(lineNo)


for key,values in words_summary.items():
	print(key, values)
'''
int(value) [27]
return [28, 30]
true [28]
except [29]
'''

