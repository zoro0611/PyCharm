import random

game_over = False
while not game_over:
    random_number = random.randint(0,10)
    print(random_number) #此公式可以驗證

    stop = False #False是代表over的意思
    while not stop: #如果stop是False的話，就執行以下的程式
        guess_number = int(input("請猜0到10之間的數字: "))
        if guess_number > random_number:
            print("您猜的有點大!!")
        elif guess_number < random_number:
            print("您猜的有點小!!")
        elif guess_number == random_number:
            print("您猜對啦，恭喜!!")
            stop = True #因為stop已經不是False，所以while迴圈不會執行