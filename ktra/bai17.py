soTien = 0
#tạo biến số tiền = 0
#tạo while vô hạn
while True:
    #gán chuỗi s = chuỗi mình vừa nhập
    s = input("Nhập nhật ký giao dịch: ")
    #tạo biến chuỗi = s.split(" ") tách ra bởi dấu cách
    chuoi = s.split(" ")
    #ví dụ: nhập: D 200
    #được chuoi[0]="D" chuoi[1]=200
    kitu = chuoi[0]
    #gán tien=int dùng để ép kiểu
    tien = int(chuoi[1])
    #Nếu kí tự = D thì tiền = tiền + tiền
    if kitu=="D":
        soTien+=tien
    #Nếu kí tự = W thì tiền = tiền - tiền
    elif kitu=="W":
        soTien-=tien
    #Nếu kí tự = E thì dừng
    #phải nhập E 0, ct mới dừng vì ở trên e default nó [kí_tự Số_tiền]
    elif kitu=="E":
        break;
print (soTien)
