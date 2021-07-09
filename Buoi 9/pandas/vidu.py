#cho tập dữ liệu sau:
#Data={"Xuat Sac":1,"Tot":2,"Trung Binh":4,"Yeu":5,"Kem":6}
#viết code xuất tập Data trên ra màn hình
import pandas as pd

Data={"Xuat Sac":1,"Tot":2,"Trung Binh":4,"Yeu":5,"Kem":6}
S=pd.Series(list(Data.values()),index = Data)
print(S)
print(S.index)
print(S.values)
