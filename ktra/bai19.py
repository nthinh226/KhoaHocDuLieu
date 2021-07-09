t = (1,2,3,4,5,6,7,8,9,10);
print("tuple ban dau: \n",t)
s=();
dem=0;
for i in range(1, 11):
    if i%2==0:
        dem+=1;
        s=s+(i,);
print("tuple chua so chan: \n",s);
