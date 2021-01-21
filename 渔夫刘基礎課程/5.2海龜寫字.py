import turtle
tina = turtle.Turtle();
tina.shape("turtle")

your_age = int(input("請輸入您的年齡: "))
if your_age >= 10 and your_age <= 15:
        tina.write("你的年齡介於10到15之間")
        tina.backward(20)
elif your_age > 15:
    tina.write("您的年齡足夠大啦!")
    tina.backward(20)
else:
    tina.write("您的年齡低於10歲，太小啦。")
    tina.backward(20)

turtle.done()

