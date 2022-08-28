import time, random

i = 1

input()

for e in range(random.randint(1, 3)):
    print("run programm")
    time.sleep(0.7)
    print("run programm.")
    time.sleep(0.7)
    print("run programm..")
    time.sleep(0.7)
    print("run programm...")
    time.sleep(0.7)
print()

while True:
    if random.randint(0, 1) == 0:
        print(random.randint(0, 1), end=" ")
    else:
        if random.randint(0, 1) == 0:
            print(random.randint(0, 1), end="  ")
        else:
            print(random.randint(0, 1), end="")

    if i >= random.randint(25, 75):
        i = 1
        if random.randint(0, 1) == 0:
            print()
        print()

    i += 1