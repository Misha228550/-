d = int(input("Введите число: "))
b = int(input("Введите число: "))
def sum_range():
    g=d+b
    if d<b:
        print(f"{b}+{d}={b+d}")
    else:
        print(f"{d}+{b}={d + b}")
sum_range()