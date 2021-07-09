#Nhập một string S, hãy tạo từ điển D trong đó key là các chữ
#xuất hiện trong S còn value tương ứng là số lần xuất hiện các chữ đó trong S.
a = (input("Nhập chuỗi: "));
dic = {};
for x in a:
    dic[x]=a.count(x);
print(dic);
