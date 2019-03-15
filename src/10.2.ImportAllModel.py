'''
当使用from module import * 时，希望对从模块或者包导出的符号进行精确的控制
可以在模块中定义一个变量__all__来明确列出需要导出的内容
'''
#10.2.ImportAllModle.py
def spam():
	pass

def grok():
	pass

blah = 42
# only export 'spam' and 'grok'
__all__ = ['spam', 'grok']

# 如果__all__定义成空列表，将没有东西被导入
# 如果__all__包含未定义的名字，在导入时会引起AttibuteError



