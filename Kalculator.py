print("1. Сложить")
print("2. Вычесть")
print("3. Умножить")
print("4. Делить")
print("Выберите опирацию:")
g = int(input(""))
if g > 4:
    print("От 1 до 4!")
    quit()
print("Введите 1 число: ")
a = int(input(""))
print("Введите 2 число: ")
b = int(input(""))
if g == 1:
    d = a+b
    print(f"{a}+{b}={d}")
if g == 2:
    l = a-b
    print(f"{a}-{b}={l}")
if g == 3:
    j = a*b
    print(f"{a}*{b}={j}")
if g == 4:
    fg = a/b
    print(f"{a}/{b}={fg}")