t = tuple()
for i in range(1,10000):
    dem=0
    #tao vong lap de thuc hien phep chia cho cac so nho hon i
    for j in range(1,i+1):
        #chia het
        if(i%j==0):
            dem=dem+1
    #dem = 2 tuc la no chi chia het cho 1 va chinh no
    if(dem==2):
    #them tuple bang cach cong tuple, co dau phay sau i de ngan cach cac phan tu
        t=t+(i,)
print(t)
