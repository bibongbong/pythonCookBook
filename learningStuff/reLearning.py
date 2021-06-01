
#re模块包含：9个常量，12个函数，1个异常，
# https://zhuanlan.zhihu.com/p/127807805

import re
'''
=========================================
re模块 常量
=========================================
'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~  re.IGNORECASE  re.I
str1 = "AbCdEfG"
pattern1 = "abcdefg"
print('默认模式：', re.findall(pattern1, str1))
print('忽略大小写模式：', re.findall(pattern1, str1, re.IGNORECASE))

'''
默认模式： []
忽略大小写模式： ['AbCdEfG']
'''


# ~~~~~~~~~~~~~~~~~~~~~~~~~  re.ASCII   re.A

#  在默认匹配模式下\w+匹配到了所有字符串，而在ASCII模式下，只匹配到了a、b、c（ASCII编码支持的字符）。
str2 = "上a下b"
pattern2 = r"\w+"  #匹配Unicode词语的字符，包含了可以构成词语的绝大部分字符，也包括数字和下划线。 + 对它前面的正则式匹配1到任意次重复
print("Unicode: ", re.findall(pattern2, str2))
print("ASCII: ", re.findall(pattern2, str2, re.ASCII))
'''
Unicode:  ['上a下b']
ASCII:  ['a', 'b']
'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~  re.DOTALL  re.S
#   DOT表示.，ALL表示所有，连起来就是.匹配所有，包括换行符\n。默认模式下.是不能匹配行符\n的
str3 = "上\n下"
pattern3 = r'.*'   #(点) 在默认模式，匹配除了换行的任意字符   * 对它前面的正则式匹配0到任意次重复， 尽量多的匹配字符串
print("默认模式: ", re.findall(pattern3, str3))
print("DOTALL模式: ", re.findall(pattern3, str3, re.S))
'''
默认模式:  ['上', '', '下', '']
DOTALL模式:  ['上\n下', '']
'''



# ~~~~~~~~~~~~~~~~~~~~~~~~~ re.MULTILINE  re.M
# 多行模式，当某字符串中有换行符\n，默认模式下是不支持换行符特性的，
str4 = "aaaaa\nbbbbb"

pattern4 = r"^bbbbb"	# ^表示匹配行的开头, 而在多行模式下，它还可以匹配 换行符\n后面的字符。
print("默认模式: ", re.findall(pattern4, str4))
print("MULTILINE模式: ", re.findall(pattern4, str4, re.M))



# 以上就是常用的常量，如果要两个一起用 | 
str4 = "aaaaa\nbbbbbC"

pattern4 = r"^bbbbbc"	# ^表示匹配行的开头, 而在多行模式下，它还可以匹配 换行符\n后面的字符。
print("默认模式: ", re.findall(pattern4, str4))
print("MULTILINE模式: ", re.findall(pattern4, str4, re.M|re.IGNORECASE))


'''
=========================================
re模块 函数
=========================================


 查找匹配项
 search - 查找任意位置的匹配项
 match  - 必须从字符串开头匹配
 fullmatch - 整个字符串与正则匹配

 查找多个匹配项
 findall - 从字符串任意位置查找，返回一个list
 finditer - 从字符串任意位置查找，返回一个iter （内存性能更优）

 分割
 

'''


