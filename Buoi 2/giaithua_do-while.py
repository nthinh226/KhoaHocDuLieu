n = int(input("Nhập số cần tính giai thừa: "))
gt=1;
i=1;
while True:
    gt=gt*i;
    i = i + 1;
    if(i > n):
        break;
    
print ('Kết quả là:',n,'!=',gt);
