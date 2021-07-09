import pandas as pd

chi_so = ["Chó", "Mèo", "chuột", "Heo", "Chim", "Cá"];
gia_tri = [20,10,50,100,120,70];
S=pd.Series(gia_tri, index=chi_so);
print(S);
print(S.index);
print(S.values);
