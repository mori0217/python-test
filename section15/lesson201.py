import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(processName)s: %(message)s')


def f(conn):
    conn.send(['test'])
    time.sleep(2)
    logging.debug("parent finished")
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(parent_conn,))
    p.start()
    # p.join()
    logging.debug(child_conn.recv())
