scoreM=input("請輸入數學成績")#輸入成績
scoreM=int(scoreM)
scoreE=input("請輸入英文成績")
scoreE=int(scoreE)
if(scoreM>=90 and scoreE>=90):#判斷有沒有獎學金
    print("獲得校長獎學金")
elif(scoreM==100 or scoreE==100):#判斷有沒有獎學金
    print("獲得校長獎學金")
else:
    print("沒有得到獎學金")

