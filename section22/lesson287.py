

import asyncio


class AwaitableClass():
    def __init__(self, message):
        self.message = message

    def __await__(self):
        print(f'Send: {self.message!r}')
        yield from asyncio.sleep(1)
        reader, writer = yield from asyncio.open_connection(
            '127.0.0.1', 8888)

        writer.write(self.message.encode())
        yield from writer.drain()

        data = yield from reader.read()
        writer.close()
        yield from writer.wait_closed()
        return data.decode()


class AsyncIterator():
    def __init__(self, message):
        self.message = message

    async def __aiter__(self):
        return self

    async def __anext__(self):
        data = await AwaitableClass(self.message)
        if data < 0:
            raise StopAsyncIteration
        return data


class AsyncContextManager():
    def __init__(self, message):
        self.enter_message = f'Enter: {message!r}'
        self.ac = AsyncIterator(message)
        self.exit_message = f'Exit: {message!r}'

    async def __aenter__(self):
        print(self.enter_message)
        await asyncio.sleep(1)
        return self.ac

    async def __aexit__(self, exc_type, exc, tb):
        print(self.exit_message)
        await asyncio.sleep(1)


async def main():
    print("start")
    async with AsyncContextManager("task1") as ac:
        async for i in ac:
            print(i)

asyncio.run(main())
