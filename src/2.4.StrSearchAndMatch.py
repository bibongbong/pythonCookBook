
#   字面字符串： str.find(), str.endswith(), str.startswith()


#   复杂的匹配： 正则表达式和re模块
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

# \d+ 表示多个数字，\d+/表示多个数字加上/
#   print yes
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

#   如果需要用同一个模式去匹配多个字符串，需要将模式字符串预编译为一个模式对象
#   同时利用括号去捕获分组，第一个括号group(1),第二个group(2),第三个括号group(3),第0个group(0)表示整个匹配到的
#   print no
datePat = re.compile('(\d+)/(\d+)/(\d+)')
if datePat.match(text2):
    print('yes')
else:
    print('no')


#   捕获分组可以使后面的处理更加方便
m = datePat.match('11/27/2018')
print(m.group(0))   #   11/27/2018
print(m.group(1))   #   11
print(m.group(2))   #   27
print(m.group(3))   #   2018
print(m.groups())   #   ('11', '27', '2018')
month, day, year = m.groups()

#   match() 只能一次寻找匹配，如果想寻找多次匹配可以用findall()
text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
for month, day, year in datePat.findall(text3):
    print('{}-{}-{}'.format(year,month,day))
    #   2012-11-27
    #   2013-3-13

for m in datePat.finditer(text3):
    print(m.groups())

