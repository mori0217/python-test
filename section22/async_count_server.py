import asyncio
import collections

counter = collections.Counter()


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()

    if counter[message] > 9:
        print(f"Received {message!r} too many times")
        counter[message] = 0
    else:
        print(f"Received {message!r}")
        counter[message] += 1
    writer.write(str(counter[message]).encode())
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
