"""
P79.栈
    class queue.LifoQueue(maxsize=0)
    LIFO即Last in First Out,后进先出。与栈的类似，使用也很简单,maxsize用法同03Queue。
    ***其实在python中不区分队列以及栈，
    只有"queue.Queue"(FIFO先进先出队列)以及"queue.LifoQueue"(LIFO后进先出队列)两种不同的队列方法。
"""
import queue
q = queue.LifoQueue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())