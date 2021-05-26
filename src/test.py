from contextlib import contextmanager
from datetime import time,datetime
start = datetime.today()
#@contextmanager
readNum = 0
def fileReaderGenerator(fn):
	#start = time.perf_counter()
	BLOCK_SIZE =  3*1024*1024
	global readNum
	with open(fn, 'r') as f:
		while True:
			block = f.read(BLOCK_SIZE)
			if block:
				readNum += 1
				yield block
			else:
				return

	#end = time.perf_counter()
	#return
#filename = "D:\\mytext.txt" # 
filename = "E:\\download\\橙红年代 - 副本.txt"
str1="刘子光"
count = 0
for i in fileReaderGenerator(filename):
	#for eachLine in i:
	#print(i)
	count += i.count(str1)
	print("count =",count)

print("count =",count)

