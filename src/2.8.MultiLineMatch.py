
#   当试图使用正则取匹配一大块文本，则需要跨多行去匹配
#   因为点号不能匹配换行符，因此可以增加对换行的支持
import re

str_pat = re.compile(r'/\*(.*?)\*/')

text1 = '/* this is a comment */'
text2 = '''/* this is a
... multiline comment */
... '''

print(str_pat.findall(text1))
#   [' this is a comment ']
print(str_pat.findall(text2))
#   []

str_pat = re.compile(r'/\*((?:.|\n)*?)\*/')
print(str_pat.findall(text2))
#   [' this is a\n... multiline comment ']

#   把 .*? 中的点号换成 (?:.|\n)
#   (?:.|\n) 指定了一个非捕获组，它定义了一个仅仅用来做匹配，而不能通过单独捕获或者编号的组

