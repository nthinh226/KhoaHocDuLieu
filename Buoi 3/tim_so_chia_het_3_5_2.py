#tìm tất cả các số trong khoảng 1-1000 sao cho: i%3,i%5,i%2 ==0
i=1;
while (i<1000):
    if (i%3==0 and i%5==0 and i%2==0):
        print(i);
    i=i+1;
