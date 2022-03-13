import random
import matplotlib.pyplot as plt

numbers_dict = {}
lst = []

STEP = 1 # Step

MIN_NUM = int(input("Enter minimal number. [DEFAULT = 0]") or 1) # Min number
MAX_NUM = int(input("Please enter maximum number. [DEFAULT = 60]") or 60)  # Max number
REPEATS = int(input("Please enter repeats quantity. [DEFAULT = 10000]") or 10000)  # How much times to randomize

RANGE = REPEATS




for i in range(RANGE):
    rand = random.randrange(MIN_NUM, MAX_NUM +1 ,STEP )
    lst.append(rand)


def count(lst):
    for k in range(MAX_NUM+1):
        numbers_dict[k] = str(lst.count(k))


count(lst)


def iterate_dict():
    for i in numbers_dict:
        print(i, ":", numbers_dict[i])

# iterate_dict()

# RENDER CHART

plt.bar(numbers_dict.keys(), numbers_dict.values())

plt.title("Randomization Anomally") # Create title
plt.xlabel('Numbers')
plt.ylabel('Count')

plt.show()
