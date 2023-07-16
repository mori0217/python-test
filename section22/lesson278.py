import asyncio

loop = asyncio.get_event_loop()


async def worker1(semaphore):
    async with semaphore:
        print("worker1 start")
        await asyncio.sleep(2)
        print("worker1 end")


async def worker2(semaphore):
    async with semaphore:
        print("worker2 start")
        await asyncio.sleep(2)
        print("worker2 end")


semaphore = asyncio.Semaphore(2)
loop.run_until_complete(
    asyncio.wait(
        [worker1(semaphore), worker2(semaphore)]
    )
)
loop.close()
