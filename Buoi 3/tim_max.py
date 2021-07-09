a=int(input("Nhập giá trị a: "));
b=int(input("Nhập giá trị b: "));
c=int(input("Nhập giá trị c: "));

max=a;
if(max<b):
    max=b;
if(max<c):
    max=c;

print("==> Giá trị lớn nhất là: ",max)
