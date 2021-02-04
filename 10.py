n=int(input("班上多少人?"))#輸入班上多少人
score=[]#建立score空陣列 紀錄數學成績
lowest=100#建立最低分預設值100
highest=0#建立最高分預設值0
highestname=""#建立最高分同學姓名
lowestname=""#建立最低分同學姓名
summath=0#建立總成績參數summath
for i in range(0,2*n):
    mathscore=input("姓名和成績多少?")
    score.append(mathscore)
    print(score)
    if i%2==1:
        score[i]=int(score[i])  
        if highest<score[i]:
            highest=score[i]
            highestname=score[i]
        if lowest>score[i]:
            lowest=score[i]
            lowestname=score[i]
        summath=summath+score[i]
print(score)
print("班上最高",highest,"是",highestname)
print("班上最低",lowest,"是",lowestname)
print("班上平均",summath/n)