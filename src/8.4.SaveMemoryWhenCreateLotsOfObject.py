'''
如果需要创建大量的对象，从而需要很大的内存
对于用来当简单的数据结构而言，可以添加__slots__属性来减少实例所占的内存
__slots__会让实例使用一个更加紧凑的，很小的固定大小的数组来构建，而不是
为每个实例定义字典

缺点是不能给实例添加新的属性，并且类也不再支持多重继承
所以应该只在经常被使用的数据结构类上定义


'''

class Date:
	__slots__ = ['year', 'month', 'day']
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

'''
不适用slots属性，直接存储一个Date实例，在64位Ptyon上需要428字节，如果使用了则下降到156字节
