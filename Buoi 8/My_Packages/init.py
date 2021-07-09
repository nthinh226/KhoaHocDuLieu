def nhap():
    a=int(input("Nhập a: "));
    b=int(input("Nhập b: "));
    print("Kết quả là: ", a+b);

def giaithua(n):
    if (n == 0):
        return 1;
    else:
        return n*giaithua(n-1);

