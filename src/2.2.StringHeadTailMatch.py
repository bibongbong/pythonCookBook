
#   通过制定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL等
#   str.starstwith(), str.endswith()

filename = 'hello.txt'
print(filename.startswith('file'))  # False
print(filename.endswith('txt')) # True

#   检查多种匹配的可能，把多种匹配项放到元组中
import os
filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
print([name for name in filenames if name.endswith(('.c', '.h'))])

#   startswith/endswith的入参必须是元组
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
print(url.startswith(tuple(choices)))   # True

#   正则表达式也可以
import  re
re.match('http:|https:|ftp:', url)