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
TIME_2 = 0
TIME_3 = 1
TIME_4 = 2
TIME_5 = 4
TIME_6 = 7
TIME_7 = 15

def newItem():
	#当前日期

	#按照记忆周期，生成该项的七个记忆点