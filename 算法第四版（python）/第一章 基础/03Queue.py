"""
P78.队列
    class Queue.Queue(maxsize=0)
    FIFO即First in First Out,先进先出。Queue提供了一个基本的FIFO容器，使用方法很简单,maxsize是个整数，指明了队列中能存放的数据个数的上限。
    一旦达到上限，插入会导致阻塞，直到队列中的数据被消费掉。如果maxsize小于或者等于0，队列大小没有限制。
    常用基本方法：
           Queue.qsize()   返回队列的大小
           Queue.empty()   如果队列为空，返回True,反之False
           Queue.full()   如果队列满了，返回True,反之False
           Queue.get([block[, timeout]])   读队列，timeout等待时间
           Queue.put(item, [block[, timeout]])   写队列，timeout等待时间
           Queue.queue.clear()   清空队列
"""
#注意这里在python3中的导入队列为queue。
#而在python2中导入队列因为Queue
import queue
q = queue.Queue()
for i in range(5):
    if (~q.full()):
        q.put(i)
while not q.empty():
    print(q.get())


