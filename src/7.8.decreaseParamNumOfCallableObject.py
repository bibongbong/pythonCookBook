
'''
如果一个callable对象，他的参数太多。如果需要减少参数个数
可以使用functools.partial()，来固定一个或多个参数的值
'''

def spam(a,b,c,d):
	print(a,b,c,d)

from functools import partial
s1 = partial(spam, 1) # a = 1
s1(2,3,4)	# 1 2 3 4
s1(4,5,6)	# 1 4 5 6 

s2 = partial(spam,1,2,d=42)	# a=1, b=2, d=42
s2(3)	# 1 2 3 42

'''
这个的使用场景是让原本不兼容的代码可以一起工作
'''

# 以[4,3]为基点，对points中个点到基点的距离进行排序
points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
import math
def distance(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return math.hypot(x2 - x1, y2 - y1)

pt = (4, 3)
points.sort(key=partial(distance,pt))
print(points) # [(3, 4), (1, 2), (5, 6), (7, 8)]

'''
如下方法也可以实现这个功能
sorted_points = sorted(points, key=lambda p:distance(pt,p))
print(sorted_points)
'''

