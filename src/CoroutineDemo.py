'''
monkey.patch_all()称为猴子补丁
提到gevent就要提下猴子补丁(monkey patch)，monkey patch指的是在运行时动态替换,
一般是在startup的时候。一般在使用gevent程序的最开头的地方会加入gevent.monkey.patch_all() ，
其作用是把标准库中的thread/socket等给替换掉。这样我们在后面使用socket的时候可以跟平常一样使用,
无需修改任何代码,但是它变成非阻塞的了。
'''

import gevent
from gevent import monkey;monkey.patch_all()
import urllib.request as request

def get_body(i):
	print('start', i)
	request.urlopen('http://cn.bing.com')
	print('end',i)
'''
# gevent.spawn启动协程，参数为函数名称和函数的参数名称
tasks = [gevent.spawn(get_body,i) for i in range(3)]

# gevent.joinall 停止协程
gevent.joinall(tasks)


start 0
start 1
start 2
end 1
end 2
end 0
'''

####################################       多线程实现       ######################################
import threading
'''
for i in range(3):
	t = threading.Thread(target=get_body, args=(i,))
	t.start()

start 0
start 1
start 2
end 0
end 1
end 2
'''

####################################       asyncio/coroutine 实现       ######################################
import asyncio

# @asyncio.coroutine把一个generator标记为coroutine类型
@asyncio.coroutine
def test(i):
	print('test start:', i)
	# 所以先输出test start，等test start输出完再输出test end

	#test()会首先打印出test_1，然后，yield from语法可以让我们方便地调用另一个generator。
	#由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
	#当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。
	#把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了
	#因此可以实现并发执行。
	r = yield from asyncio.sleep(1)
	print('test end:', i)
'''
loop = asyncio.get_event_loop()
tasks = [test(i) for i in range(5)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

test start: 4
test start: 1
test start: 2
test start: 0
test start: 3
test end: 4
test end: 2
test end: 3
test end: 1
test end: 0
'''


####################################       asyncio/await 实现       ######################################
async def test_await(i):
	print('test start:', i)
	await asyncio.sleep(1)
	print('test end:', i)


loop = asyncio.get_event_loop()
tasks = [test_await(i) for i in range(5)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''
test start: 4
test start: 1
test start: 0
test start: 2
test start: 3
test end: 4
test end: 0
test end: 3
test end: 1
test end: 2
'''