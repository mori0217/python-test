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


async def main():
    print("start")
    awaitable = await AwaitableClass("task1")
    print(awaitable)

asyncio.run(main())
