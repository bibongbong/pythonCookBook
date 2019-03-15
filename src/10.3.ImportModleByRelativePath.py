'''
想用import语句从另一个包名没有硬编码的包中导入子模块

可以使用包的相对导入，使一个模块导入同一个包的另一个模块

mypackage/
	__init__.py
	A/
		__init__.py
		spam.py
		grok.py
	B/
	__init__.py
		bar.py

如果mypackage.A.spam要导入同目录下的grok
from . import grok	

如果spam要导入不同目录下的B.bar
import ..B import bar  => ..B == ../B
'''