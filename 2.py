scoreM=input("請輸入數學成績")
scoreM=int(scoreM)
scoreE=input("請輸入英文成績")
scoreE=int(scoreE)
if(scoreM>=90 and scoreE>=90):
    print("有獎品")
elif(scoreM<90 and scoreE<90):
    print("要處罰")
else:
    print("再加油")