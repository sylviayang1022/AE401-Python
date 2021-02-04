import turtle

n=int(input("想畫幾邊形"))
hello=turtle.Turtle()
for i in range(n):
    hello.forword(100)
    hello.left(360/n)
while i<100:
    hello.forword(10+i)
    