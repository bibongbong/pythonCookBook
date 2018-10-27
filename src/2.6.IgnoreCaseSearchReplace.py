
#   以忽略大小写的方式搜索替换
#   标志参数 re.IGNORECASE
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall(r'python', text, flags=re.IGNORECASE)) #   ['PYTHON', 'python', 'Python']
print(re.sub(r'python','snake',text, flags=re.IGNORECASE))# UPPER snake, lower snake, Mixed snake

# 后面的例子，替换字符并不会跟随被替换字符的大小写保持一致
def matchCase(word):
    def replace(m):
        text = m.group
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].issupper():
            return word.capitalize()
        else:
            return word
    return replace
print(re.sub(r'python',matchCase('snake'),text, flags=re.IGNORECASE))



