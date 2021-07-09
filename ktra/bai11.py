n = int(input("nhap so luong key-value: "))
d=dict()
#nhập từ điển
for i in range(0,n):
    key=input("Key: ")
    d[key]=int(input("Values: "))

dem=0
#in ra 3 giá trị đầu tiên là values lớn nhất
for i in dl.values():
    dem+=1
    if dem<=3:
        print(i)
    else:
        break
