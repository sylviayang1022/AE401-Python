import random#輸入模組
count=0
num=random.randint(1,10)#產生數字
while count<5:
        guess=int(input("請猜數字"))#輸入數字
        count=count+1
        if num==guess:#比較
            print("答對")
            print("猜了",count,"次")
        elif guess>num:
            print("too big")
            print("猜了",count,"次")
        else:
            print("答錯")
            print("猜了",count,"次")