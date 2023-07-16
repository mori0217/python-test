import asyncio
import time
import concurrent.futures


def blocking_task(name):
    print(f'{name} starting')
    time.sleep(1)
    print(f'{name} is done')


async def main(name, loop):
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=5)

    def done_callback(future):
        print(future.result())

    for i in range(4):
        future = loop.run_in_executor(executor, blocking_task, name)
        future.add_done_callback(done_callback)
        executor.shutdown(wait=True)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([main('task', loop)]))
loop.close()
