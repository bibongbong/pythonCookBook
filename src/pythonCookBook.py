
####################################
# 1.2 解压可迭代对象，并赋值给多个变量
####################################


grades = [1, 2,3,4, 5,6,7,8,9,10]
first,*middle,last = grades
print("first:%d, middle:%s, last:%d" %(first, middle, last))
#first:1, middle:[2, 3, 4, 5, 6, 7, 8, 9], last:10


# 如果有一些用户的记录，每条记录包含一个名字，邮件，接着就是不确定数量的电话号码
record = ('Dave', 'dave@example.com', '773-22-222', '388-222-333')
name, mail, *phone_numbers = record
print("name:%s, mail:%s, last:%s" %(name, mail, phone_numbers))
#name:Dave, mail:dave@example.com, last:['773-22-222', '388-222-333']


#如果有一个公司前8个月销售数据的序列，想得到最近一个月和前面7个月的平均值的对比
*trailing_qtrs, current_qtr = grades
average = sum(trailing_qtrs)/len(trailing_qtrs)
print((trailing_qtrs,current_qtr,average))
# ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 5.0)

####################################
#  1.3 保留最后n个元素
#   使用队列
####################################

from collections import  deque

def searchMatch(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            previous_lines.append(line)
            yield line
    print('1.3: ',previous_lines)

#with open("D:/mytext.txt") as f:
#    for line in searchMatch(f, 'python', 5):
#        print(line, end='')
#        print('-'*20)

####################################
# 1.4 查找最大或者最小的n个元素
# heapq 模块的 nlargest() 和 nsmallest()
####################################

import heapq

# grades = [1, 2,3,4, 5,6,7,8,9,10]
print(heapq.nlargest(3, grades))    # [10, 9, 8]
print(heapq.nsmallest(4, grades))   # [1, 2, 3, 4]


# 更好性能的方法，将集合数据进行堆排序
# heap[0] 永远是最小的元素，但不弹出这个值
# heapq.heapify(heap) 对列表heap进行堆排序
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
for i in range(3):
    print(heapq.heappop(heap))

#先排序，再使用切片
print("切片取前4个和后3个")
print(sorted(nums)[:4])
print(sorted(nums)[-3:])

# nlargest() nsmallest() 接受关键字
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# lambda表达式用来设定nlargest的key
# 打印portfolio中price最大的前3个
print(heapq.nlargest(3, portfolio, lambda p:p['price']))


# 如果只是查找最大或者最小，用min(), max() 就可以


####################################
# 1.5 优先队列
# 按优先级排序的队列，并且每次pop操作总是返回优先级最高的元素
####################################

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # heappush的第二个参数应该是一个元组，元组的第一个元素是可排序的key值
        # 设为 -priority，目的是使priority最大的元素会被最先pop出来
        # 因为 heappop出的是key最小的元素，也就是priority最大的值的元素
        # index作为元素插入的顺序，当优先级相同时，先插入的先pop
        # 如果push时，item里没有index属性，则pop时相同优先级的元素pop顺序随机
        heapq.heappush(self._queue,  (-priority, item, self._index))
        self._index += 1

    # push pop的时间复杂度都为 O(logN), N为堆的大小
    def pop(self):
        # [2]表示返回pop出(-priority, self._index, item)里的item
        return heapq.heappop(self._queue)[1]

pq = PriorityQueue()
pq.push("tom", 2)
pq.push("jack", 7)
pq.push("mike", 1)
pq.push("mary", 4)
pq.push("john", 1)

print(pq.pop()) # 打印 jack
print(pq.pop())# 打印 mary
print(pq.pop())# 打印 tom
print(pq.pop())# 打印 mike，mike和john优先级一样，但mike先插入，其index值小
print(pq.pop())# 打印 john



####################################
# 1.6 字典中的一个键对应多个值
####################################
print("################ 1.6 字典中的一个键对应多个值 ####################")
# 最简单的办法，把多个值放到另外一个容器里，比如list或者集合
# 使用列表可以保持值的插入顺序，使用集合可以去重

a = {
    'a':[1,3],
    'b':[2,4]
}

b = {
    'c':{1,3},
    'd':{2,4}
}

# 也可以使用collections模块中的defaultdict, 它会自动初始化每个key刚开始对应的值
# 相同key的对应的其他值，插入就可以了
from collections import defaultdict

#使用list作为值的容器
#插入元素用append
d = defaultdict(list)
d['a'].append(1)
d['a'].append(1)
d['b'].append(3)
print(d) # defaultdict(<class 'list'>, {'a': [1, 1], 'b': [3]})

#使用set作为值的容器
#插入元素用add
e = defaultdict(set)
e['a'].add(1)
e['a'].add(1)
e['b'].add(3)
print(e) # defaultdict(<class 'set'>, {'a': {1}, 'b': {3}})



####################################
# 1.7 字典排序
####################################

# 要对字典排序，可以使用collections 中的 OrderedDict。
# 它会保持元素被插入时的顺序

from collections import  OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
for key in od:
    print(key, od[key])


# 如果想构建一个将来需要序列化或者编码成其他格式的映射的时候，OrderedDict非常有用
# 比如 精确控制以JSON编码后字段的顺序，就可以先用OrderedDict来构建数据
# OrderedDict内部维护着一个根据键值插入顺序排序的双向链表。每当一个新的元素插入的时候，
# 就会被放到链表的尾部

# OrderedDict的大小是普通字典的两倍，因为他维护着另一个链表，所以在使用时要考虑OrderedDict好处带来的额外内存消耗


####################################
# 1.8 字典的运算
####################################
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 字典运算，比如求最大、最小、排序等
# 当想得到字典里某个值最大的项时可能会想到用
# min(prices.values())， 但这只能得到一个值，对应的键得不到
# 只能通过迭代挨个遍历，取出最大的value
maxvalue = -float('inf')
maxValueKey = ''
for key in prices:
   if prices[key] > maxvalue:
       maxvalue = prices[key]
       maxValueKey = key
print("get max value in DICT by for: %s :%s"%(maxValueKey, maxvalue))

# 也可以使用min() max() 中提供的key函数参数来获取最大值或最小值
# 把字典prices中的每个key作为lambda的输入，得到的就是每个key的值
#key=(45.23, 612.78, 202.55, 37.20, 10.75), min(key)=10.75, 对应的就是‘FB’
# 但这也只能得到key值，要获得最小值，还要执行一遍
min(prices, key=lambda k: prices[k]) # Returns 'FB'
max(prices, key=lambda k: prices[k]) # Returns 'AAPL'
min_value = prices[min(prices, key=lambda k: prices[k])]



#  有个简单的方法
#  首先需要使用zip() 先把键和值反转过来
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
sorted_price = sorted(zip(prices.values(), prices.keys()))

#  但是
#  zip() 返回的是只能访问一次的迭代器
prices_and_names = zip(prices.values(),prices.keys())
print(min(prices_and_names)) # OK
#print(max(prices_and_names)) # ValueError:  max() arg is an empty sequence


####################################
# 1.9 查找两字典的相同点
####################################

# 可以对两字典的keys()或者items() 方法的返回结果上执行集合操作
a = {
'x' : 1,
'y' : 2,
'z' : 3
}
b = {
'w' : 10,
'x' : 11,
'y' : 2
}

# 与操作， 两字典的共有key
a.keys() & b.keys()  # {'x', 'y'}

# 差操作， 在a中但不在b中的key
a.keys() - b.keys()  # {'z'}

# 以现有字典构造一个排除特有几个指定键的新字典
c = {key:a[key] for key in a.keys() - {'z'}}
print(c)

#
#   c = {key:a[key] for key in a - {'z'}}
#   TypeError: unsupported operand type(s) for -: 'dict' and 'set'
#  for key in a 不对，应该使用for key in a.keys()
#  因为a是字典，{‘z'}是集合，字典减不了集合，a.keys()返回的是集合

# values() 类似，但并不支持集合操作。因为值视图不能保证所有值互不相同，这会导致集合操作出现问题
# 不过可以在值集合转换成set，再执行集合运算


####################################
# 1.10 删除序列中相同的元素并保持顺序
####################################
print("*****************1.10 删除序列中相同的元素并保持顺序*****************")

# 转成set，只能删除相同元素，并不能保持顺序
a = [1, 5, 2, 1, 9, 1, 5, 10]
b = list(set(a))
print(b)

#按照输入序列的顺序把元素插入set，已经有的就插入不进去，
# 生成器保证可以多次返回结果,是代码更通用，不仅仅局限于列表的处理

def deduplicate(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
c = list(deduplicate(a))
print(c)

# 如果序列中的元素不可hash，比如dict类型，需要改动
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

def deduplicateDict(items, key=None):
    seen = set()
    for item in items:
        #print("item:%s    key(item): %s "% (str(item), str(key(item))))
        value = item if key is None else key(item)
        if value not in seen:
            yield item
            seen.add(value)

# lambda的意思是，把a list中的每个元素，也就是字典元素，作为lambda的输入
# item:{'x': 1, 'y': 2}    key(item): (1, 2) ==> 插入 seen
# item:{'x': 1, 'y': 3}    key(item): (1, 3) ==> 插入 seen
# item:{'x': 1, 'y': 2}    key(item): (1, 2) ==> 已经存在，不插入 seen
# item:{'x': 2, 'y': 4}    key(item): (2, 4) ==> 插入 seen
# 把a中每个字典元素的两个key(x和y)，同时作为判断条件，同时相同才认为是相同
c = list(deduplicateDict(a, key=lambda d: (d['x'], d['y'])))
print(c)    # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]

# 把a中每个字典元素的一个key(x )作为判断条件，只要x相同就认为是这个元素是相同
d = list(deduplicateDict(a, key=lambda d: d['x']))
print(d)    # [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

# 把a中每个字典元素的一个key(y)作为判断条件，只要y相同就认为是这个元素是相同
e = list(deduplicateDict(a, key=lambda d: d['y']))
print(e)    # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]


####################################
# 1.11 命名切片
####################################
print("***************** 1.11 命名切片 *****************")

# 从一个字符串总几个固定位置提取字段
###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

# 可以给切片取个别名,避免大量无法理解的硬编码下标
# slice() 内置函数创建了一个切片对象，可以被用在任何允许使用切片的地方
SHARE = slice(20,23)
PRICE = slice(31,37)
cost = int(record[SHARE])*float(record[PRICE])

# 切片对象也有很多属性可以返回
a = slice(4,10,2)
a.start # 4
a.stop  # 10
a.step  # 2


####################################
# 1.12 序列中出现次数最多的元素
####################################
print("***************** 1.12 序列中出现次数最多的元素 *****************")

# collections.Counter 类就是为这种问题设计的。 most_common() 直接给出了答案
# Counter类可以接受任何hashable的序列
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
top_one = word_counts.most_common(1)
print("top one: %s "%top_one)   # top one: [('eyes', 8)]
top_two = word_counts.most_common(2)
print("top two: %s "%top_two)   # top two: [('eyes', 8), ('the', 5)]

# 底层实现上，Counter对象就是一个字典
print("counts for \'%s\': %d" %('look', word_counts['look']))   # counts for 'look': 4


# Counter是字典，所以可以对字典更新
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] += 1

# 或者用update（）方法
word_counts.update(morewords)

# 当然也就可以针对字典进行 + - 操作
# 再进行制表或者计数的时候，应优先使用Counter，而不是手动用字典去实现
a = Counter(words)
b = Counter(morewords)
c = a + b
d = a - b



####################################
# 1.13 通过某个关键字对字典排序
####################################
print("***************** 1.13 通过某个关键字对字典排序 *****************")

# operator模块的itemgetter函数
rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print("rows_by_fname: \n  ")
for item in rows_by_fname:
    print("%s "%item)

# lambda作为key函数，同样可以达到指定排序关键字的功能
rows_by_fname_lambda = sorted(rows, key=lambda x:x['fname'])
print("rows_by_fname_lambda: \n  ")
for item in rows_by_fname_lambda:
    print("%s "%item)


# itemgetter() 也支持多个keys
rows_by_fname_lname = sorted(rows, key=itemgetter('fname', 'lname'))
print("rows_by_fname_lname: \n  ")
for item in rows_by_fname_lname:
    print("%s "%item)

# lambda也可以指定多个key来排序
rows_by_fname_lname_lambda = sorted(rows, key=lambda x:(x['fname'], x['lname']))
print("rows_by_fname_lname_lambda: \n  ")
for item in rows_by_fname_lname_lambda:
    print("%s "%item)


# itemgetter 比lambda要稍微快一点
# itemgetter和lambda的方法同样适用于min max



####################################
# 1.14 排序不支持原生比较的对象
####################################
print("***************** 1.14 排序不支持原生比较的对象 *****************")


# 如果想对类型相同的对象排序，但这些对象不支持原生的比较操作
# 内置的sorted()有一个关键字参数key，可以传入一个callable对象，这个对象对每个传入的参数返回一个值，
# 这个值会被sorted用来排序这些对象
# 我们可以提供一个User实例作为输入，并输出对应user_id值的callable对象

# 同样两种方式， attgetter() 和 lambda
from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)



def sort_notcompare():
    users = [User(23), User(11), User(40)]
    print(users)
    print(sorted(users, key=attrgetter('user_id')))
    print(sorted(users, key=lambda u:u.user_id))

sort_notcompare()



####################################
# 1.15 通过某个字段将记录分组
####################################
print("***************** 1.15 通过某个字段将记录分组 *****************")

# 对字典或者实例的序列，根据某个特定的字段来分组迭代
# groupby() 扫描整个序列，并且查找连续相同值的元素。
# groupby 仅仅检查连续元素，如果事先没有排序，分组函数得不到想要的结果


from itertools import groupby
rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

#rows.sort(key=itemgetter('date'))
rows.sort(key = lambda r:r['date'])
for date, group in groupby(rows, key=itemgetter('date')):
    print(date)
    for item in group:
        print('  ', item)


