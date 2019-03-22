import threading
from time import sleep, ctime


balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	#print("thread {}: balance({}) +- {}".format(threading.current_thread().name,balance,n))
	balance += n	#先存
	
	balance -= n	#再取
	#print("thread {}: balance={}".format(threading.current_thread().name,balance))

def run_thread(n):
	for i in range(100000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()

t1 = threading.Thread(target=run_thread, name="t1",args=(5,))
t2 = threading.Thread(target=run_thread, name="t2",args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


def average():
	total = 0
	count = 0
	average = 0
	while True:
		temp = yield average
		total += temp
		count += 1
		average = total/count
print(type(average()))
'''
cocr1 = average()
next(cocr1)
print(cocr1.send(10))
print(cocr1.send(18))
print(cocr1.send(28))

两种方法都可以，但必须把average()赋值给cocr1
不能用average().send(item), average()每次返回的都是一个新的generator
'''
i = [10,18,28]
cocr1 = average()
print(cocr1)	# <generator object average at 0x000001B894D79B88>
print(average()) # <generator object average at 0x000001B894EBB0C0>
print(average()) # <generator object average at 0x000001B894EBB0C0>
next(cocr1)
#for item in i:
	#print(cocr1.send(item))

'''
16.4 预激活协程的装饰器
启动协程必须先激活。可以通过使用一个特殊的装饰器decorator来实现
调用 my_coro.send(x)之前必须先调用call(my_coro)
'''
from functools import wraps

def coroutine(func):
	@wraps(func)
	def primer(*args, **kwargs):
		gen = func(*args, **kwargs)
		next(gen)
		return gen
	return primer


@coroutine
def average1():
	total = 0
	count = 0
	average = None
	while True:
		temp = yield average
		total += temp
		count += 1
		average = total/count

my_coro1 = average1()
for item in i:
	print(my_coro1.send(item))

'''
16.5 终止协程
通过发送某个哨符值，让协程退出。内置的None和Ellipsis等常量是常用的哨符值
StopIterator类也可以作为哨符值

TypeError: unsupported operand type(s) for +=: 'int' and 'NoneType'
'''
my_coro2 = average1()
i1 = [10, 28, None]
#for item in i1:
#	print(my_coro1.send(item))


'''
16.6 让协程返回值
Python3.3 之前，如果生成器返回值，解释器会报语法错误
'''
from collections import namedtuple
print("-----------让协程返回值-----------")
Result = namedtuple('Result', 'count average')
def average2():
	total = 0
	count = 0
	average = None
	while True:
		temp = yield
		if temp is None:
			break
		total += temp
		count += 1
		average = total/count
	return Result(count, average)

my_coro3 = average2()
next(my_coro3)
my_coro3.send(10)
my_coro3.send(30)
my_coro3.send(6.4)

try:
	my_coro3.send(None)
except StopIteration as exc:
	result = exc.value

print(result)
'''
Result(count=3, average=15.466666666666667)
这也就正式yield from结构能在内部自动捕获StopIteration的原因
这与for循环处理StopIteration的方式一样。
yield from不但捕获StopIteration异常，还会把value属性的值变成
yield from表达式的值
'''


'''
16.7 使用yield from 
yield from类似于其他语言的await关键字。
在生成器gen中使用yield from subgen()，subgen就会获取控制权
并把产出的值传给gen的调用方，与此同时，gen会被阻塞，等待subgen终止

yield from可用来简化for循环中的yield表达式
'''

def gen():
	for c in 'AB':
		yield c
	for i in range(1,3):
		yield i

#可改写为
def gen1():
	yield from 'AB'
	yield from range(1,3)


#处理嵌套可迭代对象，类似Python CookBook 4.14
def chain(*iterables):
	for it in iterables:
		yield from it

s = 'ABC'
t = tuple(range(3))
list(chain(s,t)) # ['A', 'B', 'C', 0, 1, 2]

'''
替代产出值的嵌套for循环的功能还不足以让yield from被加入到Python
yield from的主要功能是打开双向通道，把最外层的调用方与最内层的子生成器连接起来
使得二者乐意直接发送和产出值，还可以直接传入异常。
而不用位于中间的协程中添加大量处理异常的样板代码

委派生成器 delegating generator：包含 yield from <iterable>表达式的生成器函数
子生成器 subgenerator：从yield from <iterable>表达式的<iterable>中得到的生成器
调用方 caller：调用委派生成器的客户端代码。

委派生成器在yield from表达式处暂停时，调用方可以直接把数据发给子生成器，子生成器
再把产生的值发给调用方。
子生成器返回之后，解释器会抛出StopIteration异常，并把返回值附加到异常对象
此时委派生成器就恢复了
'''
print("-----------------yield from 的使用-----------------")
#1.子生成器
def average3():
	total = 0.0
	count = 0
	average = None
	i=0
	while True:
		#2 main函数中的客户代码发送到各个值绑定到这个term上
		
		print("    average3: term = yield : ",i)
		i+=1
		term = yield
		#3 重要的终止条件，否则使用yield from调用这个协程的
		#生成器会永远阻塞
		if term is None:
			break
		total += term
		count += 1
		average = total/count
		#4 返回的Result会成为grouper中yield from表达式的值
	return Result(count, average)


#5 委托生成器
def grouper(results, key):
	#6 每次迭代会新建一个average3实例
	#每个实例都是作为协程使用的生成器对象
	i=0
	while True:
		#7 grouper发送的每个值都会经由yield from，通过管道传给average3实例
		#grouper会在yield from表达式处暂停，等待average3实例运行完毕后
		#返回的值绑定到results[key]上
		#while循环会不断创建average3实例，
		
		print("  grouper: yield from average3 : ",i)
		i+=1
		results[key] = yield from average3()

#8 客户端（调用方），驱动一切的函数
def main(data):
	results = {}
	i=0
	for key, values in data.items():
		#9 group是调用grouper函数得到的生成器对象
		#入参results用于收集结果，key是某个键
		#group作为协程使用
		
		print("main: generator grouper # : ",i)
		i+=1
		group = grouper(results, key)
		#10  预激活group协程
		next(group)
		for value in values:
			#11 把各个value传给grouper，传入的值最终到达average3
			#函数中的 term = yield
			#grouper永远不知道传入的值是什么
			print("main{}: group.send({})".format(group,value))
			group.send(value)
		#12 把None传入grouper和average3，导致当前average3实例终止
		#也让grouper继续运行，再创建一个averager3实例，处理下一组值
		group.send(None)

	print(results)
	report(results)


def report(results):
	for key, values in sorted(results.items()):
		group,unit = key.split(';')
		print('{:2} {:5} averaging {:.2f}{}'.format(result.count,group,result.average, unit))

data = {
	'girls;kg':
		[40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
	'girls;m':
		[1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
	'boys;kg':
		[39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
	'boys;m':
		[1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

main(data)		

'''
16.9 使用协程做离散事件仿真
离散时间仿真 DiscreteEventSimulation，一种把系统建模层一系列时间的仿真类型
离散事件仿真中，仿真钟向前推进的量不是固定的，比如模拟出租车运营，一个事件是顾客上车
下一个事件是顾客乘客下车。不管乘客做了5分钟还是50分钟，一旦乘客下车，仿真钟就会更新，指向此次运营结束时间

而连续仿真的仿真钟是以固定量向前推进。回合制游戏就是离散事件仿真的例子。实时游戏就是连续仿真，反应慢的玩家特别吃亏。
本节目的就是通过离散事件仿真，增进对使用协程管理并发操作的认知。洞悉asyncio、Twisted和Tornado等库
是如何在单线程中管理多个并发活动的


'''
import queue
#time事件发生时的仿真时间，proc 出租车进程实例编号，action描述活动的字符串
Event = namedtuple('Event', 'time proc action')

#每辆出租车调用一次taxi_process，创建一个生成器对象，表示每辆车的运营过程
#ident是出租车的编号，trips出租车回家前的行程数量，start_time离开车库的时间
def taxi_process(ident, trips, start_time=0):

	#离开车库，遇到yield，协程暂停，仿真主循环处理排定的下一个事件
	#当需要重新激活时，主循环用send发送当前仿真时间，赋值给time
	time = yield Event(start_time, ident, 'leave garge')
	for i in range(trips):
		#产出一个Event实例，表示拉到乘客，协程暂停，当主循环send当前时间时，重新激活这个协程
		time = yield Event(time, ident, 'pick up passenger')

		#产出一个Event实例，表示顾客下车，当主循环send当前时间时，重新激活这个协程
		time = yield Event(time, ident, 'drop off passenger')

	#行程数量完成，产出going home事件，协程最后一次暂停。
	#主循环发送时间后，协程激活并执行到最后，抛出StopIteration异常
	yield Event(time, ident, 'going home')

def compute_duration(previous_action):
    '''使用指数分布计算操作的耗时'''
    if previous_action in ['leave garage', 'drop off passenger']:
        # 新状态是四处徘徊
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        # 新状态是开始行程
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unkonw previous_action: %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1
    

class Simulator:
	def __init__(self, procs_map):
		self.event = queue.PriorityQueue()
		self.procs = dict(procs_map)

	def run(self, end_time):
		#排定各辆出租车的第一个事件
		for _,proc in sorted(self.procs.items()):
			first_event = next(proc)
			self.events.put(first_event)

		sim_time =0
		while sim_time < end_time:
			if self.events.empty():
				print('*** end of events ***')
				break

			#8
			current_event = self.events.get()

			#9
			sim_time, proc_id, previous_action = current_event
			print('taxi:',proc_id,proc_id*'  ',current_event)

			#11
			active_proc = self.procs[proc_id]

			#12
			next_time = sim_time + compute_duration(previous_action)

			try:
				#13
				next_event = active_proc.send(next_time)
			except StopIteration:
				del self.procs[proc_id]
			#send(next_time)后，如果返回的的不是StopIteration，则把next_event放到queue
			else:
				self.events.put(next_event)
		# while循环的else，到达结束时间而结束
		else:
			msg = '*** end of simulation time: {} events pending ***'
			print(msg.format(self.events.qsize()))



DEPARTURE_INTERVAL = 5
num_taxis = 3
taxis = {i: taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL) for i in range(num_taxis)}
sim = Simulator(taxis)
sim.run(end_time)
