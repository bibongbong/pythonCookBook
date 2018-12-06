'''
问题：想定义一个生成器函数，但是它会调用某个你想暴露给用户使用的外部状态值
方案：如果你想让你的生成器暴露外部状态给用户，别忘了可以简单地额将它实现为一个类，
然后把生成器函数放到__iter__()方法中去
'''

from collections import deque

class linehistory:
	def __init__(self, lines, histlen=3):
		self.lines = lines
		self.history = deque(maxlen=histlen)

	def __iter__(self):
		for lineno, line in enumerate(self.lines, 1):
			self.history.append((lineno, line))
			return line

	def clear(self):
		self.history.clear()
