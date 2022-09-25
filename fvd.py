spicok = []
def funkzua():
    N = int(input("Введите число N: "))
    for i in range(N):
        f = input("Введите имя: ")
        if f not in spicok:
            spicok.append(f)

funkzua()
print(spicok)
