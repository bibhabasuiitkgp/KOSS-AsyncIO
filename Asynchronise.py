import asyncio
import time
import aiohttp
import os


async def download(i, folder):
    url = f"https://xkcd.com/{i}/info.0.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            file = os.path.join(folder, f"file{i}.txt")   #for entering the files in folder
            os.makedirs(folder, exist_ok=True)    #for making folders
            with open(file, "w") as files:
                files.write(text)   


async def main():
    folder = "Asynchronised folder"  # Name of the folder

    start = time.time()

    obj = []
    for i in range(1, 201):
        task = asyncio.create_task(download(i, folder))
        obj.append(task)

    await asyncio.gather(*obj)

    time_taken = time.time() - start
    print("Time Taken: {0}".format(time_taken))


asyncio.run(main())


# time taken is 1.2650854587554932 seconds


                            #########    REFERENCE    ########
              # https://www.geeksforgeeks.org/python-os-path-join-method/
              # https://www.w3schools.com/python/python_file_write.asp
              # https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task
              # https://docs.aiohttp.org/en/stable/#client-example
              # https://realpython.com/async-io-python/
