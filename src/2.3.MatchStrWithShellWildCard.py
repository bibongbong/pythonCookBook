
#   使用Shell中的通配符，比如*.py,Dat[0-9]*.csv，去匹配字符串

#   fnmatch模块的 fnmatch() 和 fnmatchcase()
#   他们的功能介于简单的字符串方法和强大的正则表达式之间
#   如果只需要简单的通配符匹配， fnmatch可以满足

from fnmatch import fnmatch,fnmatchcase
fnmatch('foo.txt', '*.txt')
fnmatch('foo.txt', '?oo.txt')
fnmatch('Dat48.csv', 'Dat[0-9]*.csv')

names = ['Date.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat[0-9]*.csv')])   #  ['Dat2.csv']


#   这两个函数通常会被忽略的特性，在处理非文件名的字符串时也有用，
addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]

addr1 = [addr for addr in addresses if fnmatch(addr, '* ST')]
print(addr1)    #   ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
addr2 = [addr for addr in addresses if fnmatch(addr, '54[0-9]* *CLARK*')]
print(addr2)    #   ['5412 N CLARK ST']


