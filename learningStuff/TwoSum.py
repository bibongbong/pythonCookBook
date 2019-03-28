'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，
并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
class solution(object):
	def twoSum(self, nums, target):
		expectDict = {}
		for i in range(len(nums)):
			dif = target - nums[i]
			print(dif)
			print(nums[i])
			if nums[i] not in expectDict.keys():
				expectDict[dif] = i
				print(expectDict)
			else:
				return [expectDict.get(nums[i]),i ]

a = [2, 11, 13,7,8]
s = solution()
print(s.twoSum(a, 9))

b = [i for i in a if i%2 == 1]
print("b=", b)

for i in a:
	if i%2 == 0:
		a.remove(i)
print(a)


def get_missing_letter(srcStr):

	set1 = set(srcStr.lower())
	print(set1)
	set2 = set("abcdefghijklmnopqrstuvwzyz")
	set3 = set2-set1
	print(sorted(set3))

#get_missing_letter("A quick brown for jumps over the lazy dog")
get_missing_letter("Lions, and tigers, and bears, oh my!")


# 用一行python代码写出1+2+3+10248
from functools import reduce
c = [1, 2, 3, 10248]
sum = sum(c)
sum1 = reduce((lambda x,y:x+y), c)

''' 27 Python中变量的作用域？（变量查找顺序）
LEGB：查找的优先顺序从左到右以此是: L -> E -> G -> B
L: local 函数内部作用域
E: Enclosing 函数内部与内嵌函数之间
G： Global 全局作用域
B： build-in 内置作用域

nonlocal关键字来修改外部嵌套函数的名字空间，但是要使用 Python3才有
'''
a_var = 'global value'
def outer():
    a_var = 'enclosed value'
    print(a_var)
    def inner():
        nonlocal a_var
        a_var = 'local value'
        print(a_var)
    inner()
    print(a_var)

outer()
'''
不加 nonlocal a_var，输出：
enclosed value
local value
enclosed value

nonlocal a_var，输出：
enclosed value
local value
local value
'''



'''
28. 字符串 "123" 转换成 123，不使用内置api，例如 int()
'''
str1 = "123"
sum=0
count = 1
for s in str1:
	# sum += (ord(s)-ord('0'))*(10**(len(str1)-count))
	# count+=1
	sum = sum*10 + ord(s)-ord('0')
	print(sum)

'''
给列表中的字典排序：假设有如下list对象，
alist=[{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}],
将alist中的元素按照age从大到小排序 
[{'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}, {'name': 'a', 'age': 20}]
'''
alist=[{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}]
result = sorted(alist, key=lambda x:x['age'],reverse=True)
# alist.sort(key=lambda x:x['age'],reverse=True)
print(result)


'''
32. 该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：
1、该元素是偶数
2、该元素在原list中是在偶数的位置(index是偶数)
'''
a = [2, 11, 13,6,8]
def func_32(srcList):
	return [i for index, i in enumerate(srcList) if index%2 == 0 and index%2 == 0]
	#for index, value in enumrate(srcList):
		#if index%2 == 0 and value%2 == 0:

print(func_32(a))

'''
34. 用一行代码生成[1,4,9,16,25,36,49,64,81,100]
'''
l1 = [i*i for i in range(1,11)]
print(l1)

'''
35.输入某年某月某日，判断这一天是这一年的第几天？
'''
from datetime import datetime
def func_35(year, month, day):
	d1 = datetime(year, month, day)
	d0 = datetime(year, 1, 1)
	print(d1-d0)

func_35(2018,12,31) # 364

'''
36. 两个有序列表，l1,l2，对这两个列表进行合并不可使用extend
'''
l1 = [1, 3, 5, 7,9]
l2 = [2, 4, 6, 8, 10]
l3 = sorted(l1+l2)
print(l3)

'''
37.给定一个任意长度数组，实现一个函数
让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，
如字符串'1982376455',变成'1355798642'
'''
def func_37(l):
	return sorted(l, key=lambda x: 10+int(x) if int(x)%2==0 else int(x))
'''
key函数：如果是偶数按照 20-x来排序；如果是奇数，按本身来排序
key后，变成 1 9 12 18 3 7 14 16 5 5 
sort后，1 3 5 5 7 9 12 14 16 18 
还原key后， 1 3 5 5 7 9 8 6 4 2

同理如果，要让所有奇数都在偶数前面，而且奇数升序排列，偶数也是升序排序
sorted(l, key=lambda x: 10+int(x) if int(x)%2==0 else int(x))
'''

print(func_37('1982376455'))


'''
38.写一个函数找出一个整数数组中，第二大的数
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
import heapq
print(heapq.nlargest(2, a)[1])



def multi():
    return [lambda x : i*x for i in range(4)]
print(multi())
print([m(3) for m in multi()])