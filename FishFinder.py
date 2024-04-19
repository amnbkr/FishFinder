import requests
import random
import json

url = "http://127.0.0.1:5000/api/user"

Categories = [
    [[25000, 40000], [0.5, 15], [33, 328], [15, 24]],
    [[80000, 120000], [0.5, 20], [16, 328], [21, 30]],
    [[30000, 60000], [1, 20], [33, 328], [21, 30]],
    [[100000, 200000], [0.5, 45], [10, 164], [24, 30]],
]
random_category = random.randint(0, 3)
print(random_category)
########################################################
Frequency = str(
    random.randint(Categories[random_category][0][0], Categories[random_category][0][1])
)
Size = str(
    round(
        random.uniform(
            Categories[random_category][1][0], Categories[random_category][1][1]
        ),
        3,
    )
)
depth = str(
    random.randint(Categories[random_category][2][0], Categories[random_category][2][1])
)
Temperature = str(
    random.randint(Categories[random_category][3][0], Categories[random_category][3][1])
)

print("Freq: " + Frequency)
print("Size: " + Size)
print("depth: " + depth)
print("Temp: " + Temperature)
########################################################
myobj = {
    "user": {
        "Frequency": Frequency,
        "Size": Size,
        "Depth": depth,
        "Temperature": Temperature,
    }
}
x = requests.get(url, json=myobj)
print(x.content)
