
#   用正则表达式匹配某个文本，它找到的模式是最长可能匹配。而你想找的是最短可能匹配
#   一般出现在需要匹配一对分隔符之间的文本的时候，比如
import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))   #   ['no.']
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
#   ['no." Phone says "yes.']
#  有两对双引号，模式把最长匹配，也就是第一个双引号的开始和第二个双引号的结束之间的作为返回结果


# 模式 r'\"(.*)\"' 意思就是匹配被双引号包含的文本。
# 正则中的*操作符是贪婪的，因此匹配操作会查找最长的可能匹配，于是第二个例子返回的结果并不是沃恩想要的

# 修正：在模式中的*后面加上？
str_pat2 = re.compile(r'\"(.*?)\"')
print(str_pat2.findall(text2))

# 在一个模式字符串中，点(.)匹配除了换行外的任何字符, .* 就是匹配出换行外的任意个字符
# 如果将点号放到开始与结束符（比如引号）之间，那么匹配操作会查找符合模式的最长可能匹配
# 这回导致很多中间的被开始和结束符包含的文本被忽略
# 通常在*或者+这样的操作符后面添加一个 ? ,可以强制寻找最短可能匹配