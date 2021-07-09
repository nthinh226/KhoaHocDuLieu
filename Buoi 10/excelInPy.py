import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from xlwt.ExcelFormula import Formula

path = "C:\\Users\\dat54\\OneDrive\\Desktop\\abc.xlsx"

data = {'STT':          [1,2,3,4,5,6,7],
        'Tên':          ['Cam', 'Xoài', 'Mít', 'Ổi', 'Vải', 'Táo', 'Lê'],
        'Nơi trồng':    ['VN','Ấn Độ','VN','Nhật','VN','Mỹ','Hàn'],
        'Số lượng':     [50,75,500,192,178,300,300],
        'Giá':          [2,3,45,7,5,6,8]
        }
#print(pd.DataFrame(data)) # lấy dữ liệu của data
df = pd.DataFrame(data, columns=['STT','Tên','Nơi trồng','Số lượng','Giá']) # DF cấu trúc chữa dl 2 chiều
#region câu a: vẽ biểu đồ

#region biểu đồ hình tròn
# plt.pie(df['Số lượng'],labels=df['Tên'], autopct='%1.1f%%')
# plt.title("biểu đồ hình tròn")
# plt.show()
#endregion

#region biểu đồ hình trụ
# plt.bar(df['Tên'],df['Số lượng'],color='skyblue' )
# plt.title('biểu đồ hình trụ')
# plt.xlabel('loại quả')
# plt.ylabel('số lượng')
# plt.show()
#endregion
#endregion

#region câu b: tính tổng giá tiền cảu trái cây
print('tổng giá tiền: ',df["Giá"].sum())
#endregion

#region câu c & d: lưu dữ liệu vào file, lưu và in ra màn hình
df.to_excel(path, index=False) #cr, wr & s
print(pd.read_excel(path))
#endregion

#region câu e: cột tổng ở câu b lưu xuống file abc
df['Thành tiền'] = df['Số lượng'] * df['Giá']
print(df)
df.to_excel(path)
#endregion

#region câu f: max, min and average
#max:
print("Trái cây có giá cao nhất là: ",df['Tên'].max(),",có giá: ",df['Thành tiền'].max())
print("Trái cây có giá thất nhất là: ",df['Tên'].min(), ",có giá: ",df['Thành tiền'].min())
print("Trái cây có giá trung bình là: ",round(df['Thành tiền'].mean(),2))
#endregion