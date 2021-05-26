
#   访问列表或者元组元素一般是通过下标，但下标不易阅读。我们可以通过名称来访问元素
#   collections.namedtuple()
#   返回类型：的是标准元组类型字类的一个工厂方法
#   输入：类型名，需要的字段

from collections import namedtuple
Subscripter = namedtuple('Subscripter', ['addr', 'joined'])
sub = Subscripter("xx@xxx.com", "2018-10-12")
print(sub)  # Subscripter(addr='xx@xxx.com', joined='2018-10-12')
print(sub.addr)
print(sub.joined)

# 看起来namedtuple返回的有点像一个类实例，这个实例可以和元组互换，支持所有元组的操作，比如索引，压缩
print(len(sub))
addr,joined = sub
print(addr,joined)

# 命名元组有点像字典，可以作为字典的替代，并且所需的内存空间比字典小。
# 当需要构建一个非常大的字典结构时，命名元组的效率比字典高。缺点是命名元组和一般元组一样，不能修改，而字典可以修改

# 如果实在需要修改，可以使用_replace()方法，但返回的是一个新的命名元组，字段被新值取代
new_sub = sub._replace(addr="yy@yyy.com")
print(sub.addr) # xx@xxx.com
print(new_sub.addr) # yy@yyy.com


# 使用_replace() 来填充未被赋值元组
# *s =
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)
def dict_to_stock(s):
    print(*s)   # name shares price
    #print(**s)  # **s 是对多个参数依次调用_replace()
    return stock_prototype._replace(**s)

#  a中字段的值替换了stock_prototype中的原有几个字段的值
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a)) # Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
