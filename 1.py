score=input("請輸入成績")
score=int(score)
if(score>=60):
    print('及格')
else:
    print("不及格")
score=input("請輸入成績")
score=int(score)
if(not(score>0 and score<100)):
    print("請輸入介於0~100之間的數字")
elif(score>=90 and score<=99):
    print("A")
elif(score>=80 and score<=89):
    print("B")
elif(score>=70 and score<=79):
    print("C")
elif(score>=60 and score<=69):
    print("D")
else:
    print("E")
