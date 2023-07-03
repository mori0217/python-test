import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker1(i):
    logging.debug('start')
    time.sleep(3)
    logging.debug('end')
    return i


if __name__ == "__main__":
    with multiprocessing.Pool(3) as p:
        p1 = p.apply_async(worker1, (100,))
        p2 = p.apply_async(worker1, (100,))
        logging.debug('executed')
        print(p1.get())
        # print(p1.get(timeout=1))
        print(p2.get())
        logging.debug('finished')
