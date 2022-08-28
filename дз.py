#1
podchet = [1,2,3,4,5,6,7,8,9,10]
def dz1():
    for i in podchet:
        if int(i) % 2 == 0:
            print(i)
dz1()

#2
def dz2():
    hello = input("Напиши hello: ")
    k=i=1
    if hello == "hello":
        for i in range(0,len(hello)):
            for t in range(0,i+1):
                print(hello[i],sep=" ",end="")
            print(" ")
    elif hello == "Огурчик":
        print("молосольный)")
        quit()
    else:
        print("Я сказал введи hello!")
        quit()
dz2()