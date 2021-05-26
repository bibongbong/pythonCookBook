import multiprocessing as mp
loopNum = 10000000
def job(q):
    res = 0
    for i in range(loopNum):
        res += i + i**2 + i**3        
            
    q.put(res) # queue

def job_core1(q,lock):
    res = 0
    #lock.acquire()  # 当用到共享内存时，需要用到进程锁
    for i in range(int(loopNum/2)):
        res += i + i**2 + i**3
    
    q.put(res) # queue
    #lock.release()


def job_core2(q,lock):
    res = 0
    #lock.acquire()

    for i in range(int(loopNum/2),loopNum):
        res += i + i**2 + i**3
 
    q.put(res) # queue
    #lock.release()

#计算密集，适合用多进程
#IO密集，适合协程
def multicore():
    q = mp.Queue()
    lock = mp.Lock()
    p1 = mp.Process(target=job_core1, args=(q,lock))
    p2 = mp.Process(target=job_core2, args=(q,lock))
    p3 = mp.Process(target=job_core1, args=(q,lock))
    p4 = mp.Process(target=job_core2, args=(q,lock))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    res1 = q.get()
    res2 = q.get()
    res3 = q.get()
    res4 = q.get()
    print('multicore:',res1 + res2+res3 + res4)


import os
def job_pool(i):
    #pid = os.fork()
    global sum_global
    sum_global.value += (i + i**2 + i**3)
    #sum_global.value += (i)
    #print("pid={}:  i={},sum_global={} ".format(os.getpid(), i,sum_global.value))


def multicore_pool():
    sum_global = mp.Value('Q',0)
    pool = mp.Pool(4)
    lock = mp.Lock()
    #global sum_global
    pool.map(job_pool, range(loopNum)) #100000000
    print(sum_global.value)


import threading as td

def multithread():
    lock = mp.Lock()
    q = mp.Queue() # thread可放入process同样的queue中
    t1 = td.Thread(target=job_core1, args=(q,lock))
    t2 = td.Thread(target=job_core2, args=(q,lock))
    t3 = td.Thread(target=job_core1, args=(q,lock))
    t4 = td.Thread(target=job_core2, args=(q,lock))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    res1 = q.get()
    res2 = q.get()
    res3 = q.get()
    res4 = q.get()
    print('multithread:', res1 + res2+ res3+ res4)

def normal():
    res = 0
    for _ in range(2):
        for i in range(loopNum):
            res += i + i**2 + i**3
    print('normal:', res)      
    

import time

if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)


    multithread()
    print('multithread time:', time.time() - st1)
    #global sum_global

    st2 = time.time()
    multicore()
    print('multicore time:', time.time() - st2) 
    #st3 = time.time()
    #multicore_pool()
    #print('multicore_pool time:', time.time() - st3)   
    #print("multicore_pool: ",sum_global.value)

15625104166979167000000
15624979166729166500000    