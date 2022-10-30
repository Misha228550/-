import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Опрос")
backround = (176,196,222)
def back_rond():
    screen.fill(backround)

back_rond()

Dobrota=0
Umor=0
Chestokost=0
Trudolubivost=0
Smelost=0
Trusost=0
Odinochestvo=0
Lenivost=0
Acivki = []

print(" Вопрос 1")
print("Какие игры тебе больше всего нравятся?")
print("А.Милые и добрые, Б.Стрелялки и игры с оружием, В.Не люблю играть в игры, Г. Я занимаюсь более важными делами")
a = input("")
if a == "А" or a == "Милые и добрые":
    Dobrota+1
    Umor+1
    backround2 = (173, 255, 47)
    screen.fill(backround2)
    print(" Вопрос 2")
    print("Какие животные тебе больше всего нравятся?")
    print("А.Собаки, Б.Кошка, В.Крокодил, Г.Пингвин")
    b = input("")
    if b == "А" or b == "Собаки":
        Dobrota+1
        Trudolubivost+1
    elif b == "Б" or b == "Кошки":
        Lenivost+1
        Odinochestvo+1
        Umor+1
        Dobrota+1
    elif b == "В" or b == "Крокодил":
        Smelost+1
        Chestokost+1
        Odinochestvo+1
    elif b == "Г" or b == "Пингвины":
        Dobrota+1
        Trudolubivost+1
        Trusost+1
        Odinochestvo+1
    elif b == "Сера динозавра":
        print("Ты получил ачивку!")
        achivka2 = print("Ачивка 2 - Древнее ухо")
        Acivki.append(achivka2)
if a == "Б" or a == "Стрелялки и игры с оружием":
    Smelost+1
    Chestokost+1
    print(" Вопрос 2")
    print("Какие животные тебе больше всего нравятся?")
    print("А.Собаки, Б.Кошка, В.Крокодил, Г.Пингвин")
    b = input("")
    if b == "А" or b == "Собаки":
        Dobrota+1
        Trudolubivost+1
    elif b == "Б" or b == "Кошки":
        Lenivost+1
        Odinochestvo+1
        Umor+1
        Dobrota+1
    elif b == "В" or b == "Крокодил":
        Smelost+1
        Chestokost+1
        Odinochestvo+1
    elif b == "Г" or b == "Пингвины":
        Dobrota+1
        Trudolubivost+1
        Trusost+1
        Odinochestvo+1
    elif b == "Сера динозавра":
        print("Ты получил ачивку!")
        achivka2 = print("Ачивка 2 - Древнее ухо")
        Acivki.append(achivka2)

if a == "В" or a == "Не люблю играть в игры":
    Odinochestvo +1
    Lenivost+1
    Dobrota+1
    print(" Вопрос 2")
    print("Какие животные тебе больше всего нравятся?")
    print("А.Собаки, Б.Кошка, В.Крокодил, Г.Пингвин")
    b = input("")
    if b == "А" or b == "Собаки":
        Dobrota+1
        Trudolubivost+1
    elif b == "Б" or b == "Кошки":
        Lenivost+1
        Odinochestvo+1
        Umor+1
        Dobrota+1
    elif b == "В" or b == "Крокодил":
        Smelost+1
        Chestokost+1
        Odinochestvo+1
    elif b == "Г" or b == "Пингвины":
        Dobrota+1
        Trudolubivost+1
        Trusost+1
        Odinochestvo+1
    elif b == "Сера динозавра":
        print("Ты получил ачивку!")
        achivka2 = print("Ачивка 2 - Древнее ухо")
        Acivki.append(achivka2)
if a == "Г" or a == "Я замимаюсь более важными делами":
    Trudolubivost+1
    Dobrota+1
    print(" Вопрос 2")
    print("Какие животные тебе больше всего нравятся?")
    print("А.Собаки, Б.Кошка, В.Крокодил, Г.Пингвин")
    b = input("")
    if b == "А" or b == "Собаки":
        Dobrota+1
        Trudolubivost+1
    elif b == "Б" or b == "Кошки":
        Lenivost+1
        Odinochestvo+1
        Umor+1
        Dobrota+1
    elif b == "В" or b == "Крокодил":
        Smelost+1
        Chestokost+1
        Odinochestvo+1
    elif b == "Г" or b == "Пингвины":
        Dobrota+1
        Trudolubivost+1
        Trusost+1
        Odinochestvo+1
    elif b == "Сера динозавра":
        print("Ты получил ачивку!")
        achivka2 = print("Ачивка 2 - Древнее ухо")
        Acivki.append(achivka2)
if a == "Вась, мы же оба знаем, что я - огурец":
    print("Ты получил ачивку!")
    achivka1 = print("Ачивка 1 - Огурец")
    Acivki.append(achivka1)
    print(" Вопрос 2")
    print("Какие животные тебе больше всего нравятся?")
    print("А.Собаки, Б.Кошка, В.Крокодил, Г.Пингвин")
    b = input("")
    if b == "А" or b == "Собаки":
        Dobrota+1
        Trudolubivost+1
    elif b == "Б" or b == "Кошки":
        Lenivost+1
        Odinochestvo+1
        Umor+1
        Dobrota+1
    elif b == "В" or b == "Крокодил":
        Smelost+1
        Chestokost+1
        Odinochestvo+1
    elif b == "Г" or b == "Пингвины":
        Dobrota+1
        Trudolubivost+1
        Trusost+1
        Odinochestvo+1
    elif b == "Сера динозавра":
        print("Ты получил ачивку!")
        achivka2 = print("Ачивка 2 - Древнее ухо")
        Acivki.append(achivka2)
