x = int(input("Nhap x="));
y = int(input("Nhap y="));
j=[]
for i in range(x, y):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print (','.join(j))
