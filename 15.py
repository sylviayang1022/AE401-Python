fo=open("112.txt","r")
myletter=fo.read()
print(myletter)
fo.close()
import os.path
if os.path.isfile("112.txt"):
    print("檔案存在")
else:
    print("檔案不存在")
file=open("98.jpg","rb")
img=file.read()
file.close()
file=open("copy.jpg","wb")
file.write(img)
file.close()