import asyncio
import multiprocessing
import threading
import time


# def worker():
#     print('worker start')
#     time.sleep(2)
#     print('worker end')

loop = asyncio.get_event_loop()


# @asyncio.coroutine
# def worker():
#     print('worker start')
#     yield from asyncio.sleep(2)
#     print('worker end')


async def worker():
    print('worker start')
    # time.sleep(2)
    await asyncio.sleep(2)
    print('worker end')


def main():
    loop.run_until_complete(asyncio.wait([worker(), worker()]))
    loop.close()
    # worker()

    # t1 = threading.Thread(target=worker)
    # t2 = threading.Thread(target=worker)
    # t1.start()
    # t2.start()

    # p1 = multiprocessing.Process(target=worker)
    # p2 = multiprocessing.Process(target=worker)
    # p1.start()
    # p2.start()


if __name__ == '__main__':
    main()
