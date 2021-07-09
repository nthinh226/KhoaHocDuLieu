
msv = input("Nhap ma sinh vien: ")
t= msv+".txt"
with open(t, mode = 'w+') as f:
    f.write(input("Ho ten: ")+"\n");
    f.write(input("Ma sinh vien: ")+"\n");
    f.write(input("Gioi tinh: ")+"\n");
    f.write(input("Ngay sinh: ")+"\n");
    f.write(input("Que quan: ")+"\n");
    f.write(input("So dien thoai: ")+"\n");
    f.write(input("Facebook: ")+"\n");
f.close()

with open(t, mode = 'r') as f:
    Lines = f.readlines()
    n = len(Lines)
    for line in Lines[(n-5):]:
        #Xóa khoảng trắng ở đầu và cuối chuỗi line.strip()
        print(line.strip())
f.close()
