"""
Exercise 27: write a python program to create a queue and display all the
member and size of the queue.
The Python Standard Library: Queue
The Queue module defines the following classes and exceptions:
class Queue.Queue(maxsize=0)
    Constructor for a FIFO queue. maxsize is an integer that sets the
    upperbound limit on the number of items that can be placed in the queue.
    Insertion will block once this size has been reached, until queue items
    are consumed. If maxsize is less than or equal to zero, the queue size is
    infinite.
class Queue.LifoQueue(maxsize=0)
    Constructor for a LIFO queue. maxsize is an integer that sets the upperbound
    limit on the number of items that can be placed in the queue. Insertion will
    block once this size has been reached, unitl queue items are consumed. If
    maxsize is less than or equal to zero, the queue size is infinite.
class Queue.PriorityQueue(maxsize=0)
    Constructor for a priority queue. maxsize is an integer that sets the
    upperbound limit on the number of items that can be placed in the queue.
    Insertion will block once this size has been reached, unitl queue items are
    consumed. If maxsize is less than or equal to zero, te queue size is infinite.
Queue objects (Queue, LifoQueue, or PriorityQueue) provide the public methods
described below:
Queue.qsize()
Queue.empty()
Queue.full()
Queue.put(item, block=True, timeout=None)
Queue.put_nowait(item)
Queue.get(block=True, timeout=None)
Queue.task_done()
Queue.join()
"""
