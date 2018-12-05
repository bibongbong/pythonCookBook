'''
在正则式中使用Unicode
默认re模块已经对Unicode字符类有了基本支持，\\d 可以匹配任意的数字字符
'''

import re
num = re.compile('\d+')
print(num.match('123'))
# <_sre.SRE_Match object; span=(0, 3), match='123'>

