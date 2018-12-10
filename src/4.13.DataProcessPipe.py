'''
问题：想以管道的形式处理数据， 比如，你又大量的数据，但不能一次性将他们放到内存里
'''

import os
import fnmatch
import re

def gen_find(filepath, top):
	# top为要查找的根目录
	# path为当前查找的路径
	# dirlist为当前路径下的文件列表
	# dirlist为当前路径下的子目录列表
	#print(filepath)
	for path, dirlist, filelist in os.walk(top):
		# 返回filelist里，匹配模式filepath的集合
		print(filelist)
		for name in fnmatch.filter(filelist, filepath):
			#name为符合模式filepath的文件名
			#os.path.join()是把路径和文件名合起来
			print(os.path.join(path, name))
			yield os.path.join(path, name)
			#return os.path.join(path, name)


def gen_opener(fileName_gen):
	print('gen_opener: ', type(fileName_gen))
	for filename in fileName_gen:
		if filename.endswith('.txt'):
			f = open(filename)
			print('gen_opener: ', type(f))
			yield f
			f.close()

# Chain a sequence of iterators together into a single sequence
def gen_concatenate(file_gen):
	print('gen_concatenate 1', type(file_gen))
	for file in file_gen:
		print('gen_concatenate 2', type(file))
		# yield from file 就相当于
		#for line in file:
		#	yield line
	    # yield from 主要是用来向子生成器委派操作任务
	    # 在你想在生成器中调用其他的生成器时非常有用
		yield from file

lognames = gen_find('python*', 'c:\\jiang\\')

files = gen_opener(lognames)

lines = gen_concatenate(files)

#for line in lines:
#	print('line: ', line)

'''
上述代码的重点就是，yield语句作为数据的生产者，而for语句作为数据的消费者
当这些生成器被连在一起后，每个yield会将一个单独的数据元素传递给迭代处理管道
的下一阶段
这种方式的好处：每个生成器很小并且独立，容易编写和维护。这些函数如果通用的话，
可以在其他场景重复使用。
它的内存效率很高，即便是在超大型文件目录中也能很好工作，由于使用了迭代方式处理，
运行时只需要很小很小的内存
'''


def receiver():
	while True:
		item = yield
		print("Got", item)
recv = receiver()
# 如果不调用next(recv)，会报如下错误：
# can't send non-None value to a just-started generator
next(recv)
recv.send('hello')
recv.send('world')