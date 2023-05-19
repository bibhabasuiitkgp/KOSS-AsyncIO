import os
import time
import requests


def download(i, folder):
    url = f"https://xkcd.com/{i}/info.0.json"
    response = requests.get(url)

    text = response.text
    file = os.path.join(folder, f"file{i}.txt")   #for entering the files in folder
    os.makedirs(folder, exist_ok=True)  #for making folders
    with open(file, "w") as files:
        files.write(text)
    print(f"Page {i} downloaded")     #Just to make sure weather all the files are downloading or not as it was taking much time


def main():
    folder = "Synchronised folder"  # Specify the folder name

    start = time.time()

    for i in range(1, 201):  # Modify the range to 1-201 for 200 files
        download(i, folder)

    time_taken = time.time() - start
    print("Time Taken: {0}".format(time_taken))


main()


# time taken is 99.69449949264526 seconds

# The time difference is 98.429414033889 seconds


                             #########    REFERENCE    ########
              # https://www.geeksforgeeks.org/python-os-path-join-method/
              # https://www.w3schools.com/python/python_file_write.asp
              # https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task
              # https://docs.aiohttp.org/en/stable/#client-example
              # https://realpython.com/async-io-python/