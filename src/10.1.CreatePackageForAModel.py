'''
如何将代码组织成由很多分层模块构成的包？
在文件系统上组织你的代码，并确保每个目录都定义一个__init__.py文件，比如

graphics/
	__init__.py
	primitive/
		__init__.py
		line.py
		fill.py
		text.py
		formats/
			__init__.py
			png.py
			jpg.py

这样就可以执行import语句
import graphics.primitive.line
from graphics.primitive import line 	

__init__.py的目的是包含不同运行级别的包的可选的初始化代码
如果执行了 import graphics, 文件graphics/__init__.py将被导入，
建立graphics命名空间的内容

大部分时候__init__.py空着就好，但如果需要用来自动加载子模块
from . import jpg
from . import png
'''

