'''
如果函数很简单，仅仅只是计算一个表达式，就可以使用lambda表达式
'''

add = lambda x, y: x+y
print(add(2,3))

'''
lambda的使用场景可以是排序或数据reduce
'''
names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[0].lower()))
# 用First name排序
# ['Brian Jones', 'David Beazley', 'Ned Batchelder', 'Raymond Hettinger']

'''
lambda的使用限制，只能指定单个表示式，这个表达式的值就是返回值。
不能有多个语句、条件表达式、迭代、异常处理
'''

