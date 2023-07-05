import concurrent.futures
import logging
import time

# logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def worker(x, y):
    logging.debug('start')
    time.sleep(2)
    r = x*y
    logging.debug(r)
    logging.debug('end')
    return r


def main():
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # f1 = executor.submit(worker, 2, 5)
    # f2 = executor.submit(worker, 20, 50)
    # logging.debug(f1.result())
    # logging.debug(f2.result())

    # args = [[2, 20], [5, 50]]
    # r = executor.map(worker, *args)
    # logging.debug(r)
    # logging.debug([i for i in r])

    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        # f1 = executor.submit(worker, 2, 5)
        # f2 = executor.submit(worker, 20, 50)
        # logging.debug(f1.result())
        # logging.debug(f2.result())

        args = [[2, 20], [5, 50]]
        r = executor.map(worker, *args)
        logging.debug(r)
        logging.debug([i for i in r])


if __name__ == "__main__":
    main()
