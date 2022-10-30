def summa(a,b):
    print("1. Сложить")
    d = a + b
    print(f"{a}+{b}={d}")
def Vichitanie(a,b):
    print("2. Вычесть")
    l = a - b
    print(f"{a}-{b}={l}")
def umnochenie(a,b):
    print("3. Умножить")
    j = a * b
    print(f"{a}*{b}={j}")
def delenie(a,b):
    print("4. Делить")
    fg = a / b
    print(f"{a}/{b}={fg}")
def more_funkcia():
    print("А зачем...? Ну ладно")
    print("1. Выйти")
    print("2. Вернуться к  калькулятору")
    print("3. Какой-то вопрос")
    print("4. Функция - (Я увидел ошибку)")
    print("Выберите функцию")
    gg = int(input(""))
    if gg == 1:
        quit()
    elif gg == 2:
        print("Ладно, заново...")

    elif gg == 3:
        print("Задавайте его!")
        f = input("")
        if f == "Да":
            print("Ууупс... ERROR 404")
            quit()
        else:
            print("Ууупс... ERROR 404")
            quit()
    elif gg == 4:
        print("Если вы каким-то способом нашли ошибку, то сообщите о ней на этом сайте:")
        print("https://www.youtube.com/watch?v=urMo0COpCo8")
        quit()
    else:
        print("Надо было выбрать, то, что довали!")
        more_funkcia()

#главная ф-ия
while True:
    print("1. Сложить")
    print("2. Вычесть")
    print("3. Умножить")
    print("4. Делить")
    print("Выберите опирацию:")
    g = int(input(""))
    if g > 4:
        print("От 1 до 4!")
        continue
    print("Хотите какую другою опирацию?")
    print("Нет - 0, да - 1")
    m = int(input(""))
    if m == 0:
        print("Введите 1 число: ")
        a = int(input(""))
        print("Введите 2 число: ")
        b = int(input(""))
        if g == 1:
            summa(a,b)
        if g == 2:
            Vichitanie(a,b)
        if g == 3:
            umnochenie(a,b)
        if g == 4:
            delenie(a,b)
    else:
        more_funkcia()
