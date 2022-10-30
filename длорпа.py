spicor1 = [1, 2, 3, 4, 5]
print(spicor1)
print(spicor1[2:4])

import random
spicok2 = []
print(spicok2)
for i in range(10):
    a = random.randint(1,100)
    spicok2.append(a)
print("тут рандомные числа")
print(spicok2)
print("Стереть код?")
print("да/нет")
i = input("")
if i == "да":
    spicok2.clear()
    print(spicok2)
    spicok2.append("Тут ничего нет")
    print(spicok2)
    quit()
elif i == "нет":
    print("ок, не буду")
    print(spicok2)
else:
    quit()
