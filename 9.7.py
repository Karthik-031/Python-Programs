f=open("C:\\Users\\Administrator\\Desktop\\demo.txt",'r')
print("The filepointer is at byte:",f.tell())
f.seek(10);
print("after reading , the filepointer is at :",f.tell())
