import requests
import asyncio
import aiohttp


async def task(delay: int):
    await asyncio.sleep(delay)
    print("TASK execution, finished!")


async def fetch_data(url: str):
    async with aiohttp.ClientSession() as session:
        print(f"Fetching data ...")
        response = await session.get(url, ssl=False)
        data = await response.text()
        print(f"Finished fetching data!")
        return data

    # with requests.Session() as session:
    #     print(f"Fetching data ...")
    #     response = session.get(url)
    #     data = response.text
    #     print(f"Finished fetching data!")
    #     return data


async def main():
    url = "https://raw.githubusercontent.com/litterinchina/large-file-download-test/refs/heads/master/10M.txt"

    await asyncio.gather(
        fetch_data(url),
        task(2)
    )


asyncio.run(main())