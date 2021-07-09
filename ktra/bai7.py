with open("a.txt",mode='r+',encoding='utf-8')as f:
    s=f.read();
    dic={};
    d=0;
    for i in s:
        dic[s[d]]=s.count(i);
        d=d+1;
print(dic);
dic_sort = sorted(dic.items(),reverse=True, key = lambda x:x[1]);
print(dic_sort);
f.close();

//Thầy giải
f = open("./data.txt", "r")
content = f.readline()
count = {}
for i in content:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

sorted(count.values(), reverse=True)

print(count)
