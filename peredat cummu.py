spicok = []
def summa_funkzii(h):
    kol = 0

    d = int(input("Число 1: "))
    j = int(input("Число 2: "))
    p = int(input("Число 3: "))
    h.extend((d, j, p))
    for i in h:
        kol+=i
    if kol == 5:
        print("Дейв: Today good weather, dosn't it?")
    elif kol == 0:
        print("Дейв: How you plus 0?")
    elif kol == 8:
        print("Дейв: 8 - it's number")
    elif kol == 22:
        print("Buf Buf")
    elif kol == 3879:
        print("Дейв: Who you doing that?!")
    elif kol == 777:
        print("Дейв: Не пытайся, пожалуйста...")
        tell = input("ДАВАЙ:")
        if tell == "я хочу рассказать историю о зайце":
            print("Дейв: Зря ты так")
            print("BANED")
        elif tell == "No":
            print("Дейв: Rub Tub - cu-tu-be")
            tuub = input("")
            if tuub == "Tub Rub":
                print("ачивка 1")
            else:
                print("BANED")
        else:
            print("Дейв: ну ок")
    elif kol == 2000:
        print("Дейв: NONONONONOON")
        a = input("КОД: ")
        if a == "КвадратныйАнанас":
            print("Квадратн6ый Мотоц8кл")
            pipai = input("ПАПАИ: ")
            if pipai == "Не Дерево":
                print("куст 255 888 932")
                cod583 = int(input("SEREDINA: "))
                if cod583 == 583:
                    print("Дейв: OMG, YOU CAN WIN!")
                    fife = input("Смешарики, Лосось, баран333: ")
                    if fife == "Шар, Лось, овцааа":
                        print("Дейв: YOU WIN!!")
                        print("*Звуки появления приза*")
                        print("ачивка 2")
                    else:
                        print("Game Over!!!! (А ты был так близок...)")
                else:
                    print("Game Over!!!!")
            else:
                print("Game Over!!!!")
        else:
            print("Game Over!!!!")

    return kol

print(summa_funkzii(spicok))



