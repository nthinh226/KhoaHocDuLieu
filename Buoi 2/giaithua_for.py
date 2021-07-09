n = int(input("Nhập số cần tính giai thừa: "))
gt=1;

for x in range(1,n+1):
    gt=gt*x;
    
print ('Kết quả là:',n,'!=',gt);
