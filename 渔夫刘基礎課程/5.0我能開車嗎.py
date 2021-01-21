driving_age = int(input("請輸入開車的合法年齡: ")) #把用戶輸入的文字變成了數字
your_name = int(input("請輸入您的年齡: "))
if your_name >= driving_age:
    print("恭喜您, 您的年齡可以合法開車。")
else:
    print("很抱歉，您的年齡太小，不能開車。")
    print("再等兩年吧。")
