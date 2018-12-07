'''
问题：如果想遍历一个可迭代对象，但它开始的元素不敢兴趣，想跳过
方案：itertools.dropwhile()
使用时，给它传递一个函数对象和一个可迭代对象，他会返回一个迭代器对象，
丢弃原有序列中的元素，知道函数返回Flase，然后再返回后面接下来的所有元素
'''

# 读取文件，但跳过里面以 # 开头的注释部分，但只是跳过开头，中间的不跳过
#from itertools import dropwhile
#from itertools import ifilter


with open('1.16.filterSequence.py', encoding='UTF-8') as f:

	# 有多种方式实现这个功能： 把前面以 # 开始的行过滤
	# 1. dropwhile
	#for line in dropwhile(lambda line: line.startswith("#"), f):
	#	print(line)
	
	# 2. filter
	# itertools.ifilter 从python3里删除，改为filter()函数
	# 这个不仅过滤开头几行注释，连中间的注释也过滤掉
	for line in filter(lambda line: not line.startswith("#"), f):
		print(line)
	
	# 3. for 循环
	#for line in f :
	#	if not line.startswith('#'):
	#		print(line)

	# 4. 列表解析
	#linesNoComments = [line for line in f if not line.startswith('#')]
	#print(linesNoComments)