
#   需要将一个字符串分割为多个字段，但是分隔符并不是固定的
#   string.split() 只适用于非常简单的字符串分割，但并不支持多个分隔符以及分隔符周围的空格
#   解决方案： re.split()

import re
line = 'asdf fjdk; afed, fjek,asdf, foo'

#   这个正则的意思是，分隔符可以是分号，逗号，空格，并且后面紧跟着若干个空格
print(re.split(r'[;,\s]\s*', line))

#   如果正则里包含一个括号，则这个括号叫捕获分组，
#   和上面的区别就是，分隔符也被提取出来
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]    # 从第一个元素开始取，step为2  ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
delimiters = fields[1::2]+['']   # 从第二个元素开始取，step为2  [' ', ';', ',', ',', ',', '']
back = ''.join(v+d for v, d in zip(values,delimiters))
print(back)

#   如果不想保留分隔符到结果列表中，但仍然需要括号来分组正则表达式





