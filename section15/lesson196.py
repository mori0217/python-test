import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker1(i):
    logging.debug('start')
    logging.debug(i)
    time.sleep(3)
    logging.debug('end')


def worker2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


if __name__ == "__main__":
    i = 10
    p1 = multiprocessing.Process(name="rename worker1", target=worker1, args=(i,))
    p1.daemon = True
    p2 = multiprocessing.Process(target=worker2, args=(i,))
    p1.start()
    p2.start()
    print('started')
    p1.join()
    p2.join()
    print('joined')
