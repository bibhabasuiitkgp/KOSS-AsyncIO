import asyncio
import time
import aiohttp


async def download(i):
    url = f"https://reqres.in/api/users?page{i}"     #url for the page
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()            #storing the content in 'text'
            file = f"file{i}.txt"                   #giving the file name
            with open(file, "w") as files:
                files.write(text)

    await asyncio.sleep(i)


async def main():
    obj1 = download(1)
    obj2 = download(2)
    obj3 = download(3)

    start = time.time()

    await asyncio.gather(obj1, obj2, obj3)   #Creates a single object of obj1,obj2,obj3 that allows us to do execution concurrently

    time_taken = time.time() - start
    print("Time Taken: {0}".format(time_taken))


asyncio.run(main())