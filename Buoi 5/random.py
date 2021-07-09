#random 10 so chia het cho 3,5 nhung k chia het cho 2
import random;
s=0;
while s<10:
    x=random.randint(1,100);
    if (x%3==0 and x%5==0 and x%2!=0):
        s=s+1;
        print(x);



