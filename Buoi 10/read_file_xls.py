import pandas as pd
xl = pd.ExcelFile('data.xlsx')

#dữ liệu data
data = [[1,"Cam",'VN',50,2],
    [2,'Xoài','Ấn Độ',75,3],
    [3,'Mít','VN',178,5],
    [4,'Ổi','Nhật',192,7],
    [5,'Vải','VN',178,5],
    [6,'Táo','Mỹ',300,6],
    [7,'Lê','Hàn Quốc',200,8]]

"""#b in ra tổng tiền
for i in range(len(data)):
    print("tổng tiền: ",data[i][1],"=",data[i][3]*data[i][4])
"""


df=pd.DataFrame(data, columns=['STT','Tên','Nơi Trồng','Số Lượng','Giá'])
#Lưu vào file xl = pd.ExcelFile('data.xlsx')
df.to_excel(xl, sheet_name = "data", index=False)

print(pd.read_excel(xl))

#e cột tổng ở câu b lưu xuống file abc
df = pd.read_excel(xl)
df['Tổng'] = df['Số Lượng'] * df['Giá']
print(df)
df.to_excel(xl)

"""
#f max, min, average
print("Trái cây có giá cao nhất là: ",df['Tên'].max(),df['Tổng'].max())
print("Trái cây có giá thất nhất là: ",df['Tên'].min(),df['Tổng'].min())
print("Trái cây có giá trung bình là: ",round(df['Tổng'].mean(),2))
"""
