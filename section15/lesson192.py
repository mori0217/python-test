import logging
import threading
import time
import queue

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')


# def worker1(queue):
#     logging.debug('start')
#     queue.put(100)
#     time.sleep(2)
#     queue.put(200)
#     logging.debug('end')


# def worker2(queue):
#     logging.debug('start')
#     logging.debug(queue.get())
#     logging.debug(queue.get())
#     logging.debug('end')


# if __name__ == "__main__":
#     queue1 = queue.Queue()
#     t1 = threading.Thread(target=worker1, args=(queue1, ))
#     t2 = threading.Thread(target=worker2, args=(queue1, ))
#     t1.start()
#     t2.start()

def worker1(queue):
    logging.debug('start')
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()
    time.sleep(2)
    logging.debug('end')


if __name__ == "__main__":
    queue1 = queue.Queue()
    for i in range(10000):
        queue1.put(i)
    ts = []
    for _ in range(3):
        t = threading.Thread(target=worker1, args=(queue1, ))
        t.start()
        ts.append(t)
    logging.debug('tasks are not done')
    queue1.join()
    logging.debug('tasks are done')
    for _ in range(len(ts)):
        queue1.put(None)
    [t.join() for t in ts]
