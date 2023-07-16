import asyncio


async def tcp_echo_client(message):
    print(f'Send: {message!r}')
    await asyncio.sleep(1)
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    writer.write(message.encode())
    await writer.drain()

    data = await reader.read()
    writer.close()
    await writer.wait_closed()
    return data.decode()


async def main():
    elapsed = await asyncio.gather(
        asyncio.create_task(tcp_echo_client("task1")),
        asyncio.create_task(tcp_echo_client("task2")),
    )

    print(elapsed)


asyncio.run(main())
