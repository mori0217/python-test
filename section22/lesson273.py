import asyncio
import time

import aiohttp
import requests

loop = asyncio.get_event_loop()


# async def get(url):
#     print(requests.get(url).content)
#     print(time.time())

async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)
            print(time.time())
    # await asyncio.sleep(2)

loop.run_until_complete(asyncio.wait([
    get("http://httpbin.org/headers"),
    get("http://httpbin.org/headers"),
]))
