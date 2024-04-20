import requests
import random
import json
from time import sleep

url = "http://127.0.0.1:5000/api/user"

MIN = 0
MAX = 1
FREQUENCY = 0
SIZE = 1
DEPTH_ = 2
TEMPERATURE = 3
Categories = [
    [[25000, 40000], [0.5, 15], [33, 328], [15, 24]],
    [[80000, 120000], [0.5, 20], [16, 328], [21, 30]],
    [[30000, 60000], [1, 20], [33, 328], [21, 30]],
    [[100000, 200000], [0.5, 45], [10, 164], [24, 30]],
]
########################################################
while True:
    random_category = random.randint(0, 3)
    print("Category: " + str(random_category))
    Frequency = str(
        random.randint(
            Categories[random_category][FREQUENCY][MIN],
            Categories[random_category][FREQUENCY][MAX],
        )
    )
    Size = str(
        round(
            random.uniform(
                Categories[random_category][SIZE][MIN],
                Categories[random_category][SIZE][MAX],
            ),
            2,
        )
    )
    depth = str(
        random.randint(
            Categories[random_category][DEPTH_][MIN],
            Categories[random_category][DEPTH_][MAX],
        )
    )
    Temperature = str(
        random.randint(
            Categories[random_category][TEMPERATURE][MIN],
            Categories[random_category][TEMPERATURE][MAX],
        )
    )

    print("Freq: " + Frequency)
    print("Size: " + Size)
    print("depth: " + depth)
    print("Temp: " + Temperature)
    ########################################################
    myobj = {
        # "user": {
        "Frequency": Frequency,
        "Size": Size,
        "Depth": depth,
        "Temperature": Temperature,
        # }
    }
    x = requests.post(url, json=myobj)
    # print(x.content)

    sleep_time = random.randint(1, 3)
    print("Sleep Time: " + str(sleep_time))
    print("########################################################")
    sleep(sleep_time)
