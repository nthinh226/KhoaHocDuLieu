dic={};

t=0;

while(t<5):

    for x in range(10):

        if(x%2==0):

            dic[t]=x;

            t=t+1;


print(dic);
dic1={};
print("Số chia hết cho 3 trong dict: ");
for i in dic:

    if(dic[i]%3==0):

        dic1[i]=dic[i];
print(dic1);
