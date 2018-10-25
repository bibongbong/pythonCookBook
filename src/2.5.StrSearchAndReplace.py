
#   在字符串中搜索和替换指定的字符串
#   str.replace()

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

#   复杂的情况，可以使用re模块的sub函数
#   sub的第一个参数是被匹配的模式，第二个是替换模式，\3表示前面模式的匹配组号
import re
text1 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
text2 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text1)
print(text2)    #   Today is 2012-11-27. PyCon starts 2013-3-13.

#   如果匹配模式需要复用
datapa = re.compile(r'(\d+)/(\d+)/(\d+)')
text3 = datapa.sub(r'\3.\1.\2', text1)
print(text3)    #   Today is 2012.11.27. PyCon starts 2013.3.13.

#   更复杂的模式，可以传递一个替换回调函数
#   这里datapa这个匹配模式的匹配结果是作为change_date() 的入参m
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datapa.sub(change_date, text1))   #   Today is 27 Nov 2012. PyCon starts 13 Mar 2013.


#   如果想直到被替换多少次，re.subn()
newText, n = datapa.subn(change_date, text1)
print(newText,n)    #   n = 2