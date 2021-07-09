"""
str = input("Nhập chuỗi: ")
chuHoa = 0
chuThuong = 0
for i in str:
    if('a'<=i<='z'):
        chuThuong+=1
    elif('A'<=i<='Z'):
        chuHoa+=1
print(chuHoa)
print(chuThuong)

"""
chu = input('Vui lòng nhập chuỗi: ')
chuHoa, chuThuong = 0, 0
for i in range(len(chu)):
    if (chu[i].islower()):
        chuThuong += 1
    elif(chu[i].isupper()):
        chuHoa += 1
    else:
        continue;
print('Số chữ hoa:', chuHoa, 'chữ', '-', 'Số chữ thường:', chuThuong, 'chữ')
