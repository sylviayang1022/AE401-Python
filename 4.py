import random#輸入模組
num=random.randint(1,10)#產生數字
guess=int(input("請猜數字"))#輸入數字
if num==guess:#比較
    print("答對")
else:
    print("答錯")
    print("答案是",num)