import random
from time import sleep
file = open("c:/Users/Sven/Documents/Projecten/read-files/README.md", "r")

list = file.readlines()

for i in range(20):
    print(list[random.randint(0, 18)])
    sleep(1)
