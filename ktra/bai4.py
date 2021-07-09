#nhập chuỗi cần đếm
n = input("Chuoi: ")

d=dict()
#Thực hiện đếm và gán luôn vào từ điển
for i in n:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)
