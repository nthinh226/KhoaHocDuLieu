#tạo từ điển D 5 phần tử, giá trị tuỳ chọn. Lấy từng phần tử bỏ vào tập set.
D = {}; 
for x in range(2,7):
    D[x]=x*x;

print(D);

myset = set();

for x in D:
    myset.add(D[x]);
print(myset);
