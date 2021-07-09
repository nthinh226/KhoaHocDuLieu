n = int(input("nhap so luong key-value: "))
d=dict()
#nhập từ điển
for i in range(0,n):
    key=input("Key: ")
    d[key]=int(input("Values: "))
dl={}
#sắp xếp theo giá trị value giảm dần
for i in sorted(d,key=d.get,reverse = True):
    dl[i]=d[i]
print(dl)
#bien dem
dem=0
#in ra 3 giá trị đầu tiên là values lớn nhất
for i in dl.values():
    dem+=1
    if dem<=3:
        print(i)
    else:
        break
