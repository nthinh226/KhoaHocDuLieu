#tạo tuple 5 số nguyên, vừa chia hết cho 3, 5
count=0;
t=();
while True:
    for x in range(0,1000):
        if(x%3==0 and x%5==0):
            count=count+1;
            if(count<=5):
                t=t+(x,);
            else:
                print(t);
                break;
    break;
            
    

