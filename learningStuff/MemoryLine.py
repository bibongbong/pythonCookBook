import datetime

'''
记忆曲线
记忆周期：
第一周期：当天，
第二周期：当天12小时后（睡前）
第三周期：第一天，
第四周期：第二天，
第五周期：第四天，
第六周期：第七天，
第七周期：第十五天
'''

TIME_1 = 0
TIME_2 = 8
TIME_3 = 1*24
TIME_4 = 2*24
TIME_5 = 4*24
TIME_6 = 7*24
TIME_7 = 15*24
MEMORY_POINT = [TIME_1, TIME_2, TIME_3, TIME_4, TIME_5, TIME_6, TIME_7]
MAX_NUM_OF_MEMORY_TIME = 7
ALL_Item = []

class MemoryItem:
	
	def __init__(self, src_name, src_startDateTime):
		self.memoryList = []
		self.name = src_name
		self.startDateTime = src_startDateTime


		#按照记忆周期，生成该项的七个记忆点
		for i in range(MAX_NUM_OF_MEMORY_TIME):
			delta = datetime.timedelta(hours=MEMORY_POINT[i])
			self.memoryList.append(self.startDateTime+delta)

	def __str__(self):
		temp = []
		temp.append(self.name)
		for i in self.memoryList:
			temp.append(i.strftime("%Y-%m-%d %H:%M")) 
		return '\n'.join(temp)


	



#判断当前日期时间，检查复习计划表，如果到则发出通知
def notify():
	pass


a = MemoryItem('itme1', datetime.datetime.now())
b = MemoryItem('itme2', datetime.datetime.now()+datetime.timedelta(days=1))
c = MemoryItem('itme2', datetime.datetime.now()+datetime.timedelta(days=2))
d = MemoryItem('itme2', datetime.datetime.now()+datetime.timedelta(days=3))
ALL_Item.append(a)
ALL_Item.append(b)
ALL_Item.append(c)
ALL_Item.append(d)
for i in ALL_Item:
	print(i)
