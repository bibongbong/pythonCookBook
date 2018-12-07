#  对一个序列，想提取其中需要的部分，或者缩短序列
#  1. 列表推导
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
shortList = [n for n in mylist if n > 0]
print(shortList)

#   列表推导的缺点：如果输入很大，会产生一个非常大的结果集，占用大量内存
#   2. 生成器
def getShortList(mylist):
    for n in mylist:
        if n > 0:
            yield n
# 不能直接使用：
# shortListByYield = getShortList(myList)
# 因为 getShortList() 返回的是一个生成器，不是一个list
# 两种从生成器转换成list的方法，列表推导和list函数都可以
#shortListByYield = [n for n in getShortList(mylist)]
shortListByYield = list(getShortList(mylist))
print(shortListByYield)

#   当过滤条件比较复杂，列表推导或者生成器不能满足需求时可以使用
#   3. 内建 filter() 函数
#   filter() 第一个参数是过滤函数，第二个是需要被过滤的列表
#   列表里的元素挨个传入，返回True时，该元素pass，返回False的元素被过滤掉
def is_int(value):
    try:
        x = int(value)
        return True
    except ValueError:
        return False
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
valList = list(filter(is_int, values))
print(valList)  # ['1', '2', '-3', '4', '5']


#  过滤操作还可以把不符合条件的元素替换掉
#  当列表推导中的if/else在for前面的时候表示从valuelist取出值以后的操作
#  当列表推导中的if/else在for后面的时候表示在valuelist中取值时的取值条件
valuelist = [1, 4, -5, 10, -7, 2, 3, -1]
pos_list = [n if n > 0 else 0 for n in valuelist]
neg_list = [n if n < 0 else 0 for n in valuelist]
print(pos_list) # [1, 4, 0, 10, 0, 2, 3, 0]


#   itertools.compress(), iterable对象和Boolean选择器序列作为输入
#   输出 iterable中对应Boolean选择器为True的元素的迭代器
#   用途：用另一个相关联的序列来过滤某个序列

from itertools import compress
addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK',
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

# more_than_5中第2/5/6个元素为True，那么compress返回的就是addresses中第2/5/6个元素
# 这里的关键就是Boolean序列，指出哪些元素符合条件。有点像蒙版
# compress() 返回的时迭代器，所以如果需要得到序列，需要用list()
more_than_5 = [n > 5 for n in counts]   # [False, False, True, False, False, True, True, False]
filered_add = list(compress(addresses, more_than_5))    #['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
print(filered_add)
