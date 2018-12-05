'''
在处理Unicode字符串时，需要确保所有字符串在底层有相同表示
'''

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
#'Spicy Jalapeño'
print(s1)
#'Spicy Jalapeño'
print(s1 == s2)
False
print(len(s1))
# 14
print(len(s2))
# 15


'''
字符串的多种表达会产生如上问题，我们可以使用unicodedata模块，将文本标准化
NFC表示字符是整体组成，比如可能的话就使用单一编码；NFD表示字符应该分解为多个组合字符表示
另外Python还有NFKC和NFKD等标准
'''
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1)) # 'Spicy Jalape\xf1o'

t3 = unicodedata.normalize('NFD', s1)
print(ascii(t3)) #'Spicy Jalapen\u0303o'


'''
在清理和过滤文本的时候字符的标准化也很重要。比如，需要清除一些文本上的变音符
combining()用于测试一个字符是否为和音字符
'''
t4 = unicodedata.normalize("NFD", s1)
print(''.join(c for c in t4 if not unicodedata.combining(c)))
# Spicy Jalapeno
