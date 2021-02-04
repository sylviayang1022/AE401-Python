n=int(input("班上多少人?"))
score=[]
name=[]
lowest=100
highest=0
highestname=""
lowestname=""
summath=0
for i in range(n):
    mathname=input("name?")
    mathscore=int(input("mathscore?"))
    name.append(mathname)
    score.append(mathscore)
    if highest<mathscore:
        highest=mathscore
        highestname=mathname
    if lowest>mathscore:
        lowest=mathscore
        lowestname=mathname
    summath=summath+mathscore
print(score)
print(name)
print("班上最高",highest,"是",highestname)
print("班上最低",lowest,"是",lowestname)
print("班上平均",summath/n)