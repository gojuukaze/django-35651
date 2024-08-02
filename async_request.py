import asyncio

import aiohttp


async def fetch(session):
    async with session.get('http://127.0.0.1:8000/test') as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(10):
            tasks.append(fetch(session))
        await asyncio.gather(*tasks)


asyncio.run(main())
