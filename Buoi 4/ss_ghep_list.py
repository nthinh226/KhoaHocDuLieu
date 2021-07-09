def cmp(a,b):
    return(a>b)-(a<b);

list1=[0,1,3];
list2=[5,5,3];


if(cmp(list1,list2)>0):
    print("List 1 lớn hơn List 2");
elif(cmp(list1,list2)==0):
    print("List 1 bằng List 2");
else:
    print("List 1 nhỏ hơn List 2");
    

print("Tong list 1=",sum(list1));
print("Tong list 2=",sum(list2));

list3=list1;
list3.extend(list2);
print("Ghep list: ",list3);
