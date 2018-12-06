'''
删除字符串中不需要的字符
比如去掉字符串开头，结尾和中间的不想要的字符
strip()用于删除开始和结尾的字符。lstrip和rstrip分别从左和右执行删除。
默认会去除空白字符，也可以删除指定字符
'''

s = ' hello world \n'
print(s.strip()) # hello world
print(s.lstrip()) # hello world \n
print(s.rstrip()) #  hello world

t = '-----hello===='
print(t.lstrip('-')) # hello====
print(t.rstrip('=')) # -----hello

'''
strip只能从两头对字符串进行修剪，如果要对字符串中间进行处理替换，要用replace，或者正则表达式
'''

print(s.replace(' ', '')) # helloworld

import re
s1 = re.sub('\s+', '-', s)
print(s1) # -hello-world-

'''
 从文件中读取多行数据，然后逐行修剪
 表达式 lines = (line.strip() for line in f)是一个生成器，这样很高效
 它不需要预先读取所有数据放到一个临时的列表，它创建一个生成器，每次返回行之前会执行strip
 '''

with open('2.1.StringSplit.py', encoding='UTF-8') as f:
	#lines = (line.strip() for line in f)
	for line in f:
		print(line)
