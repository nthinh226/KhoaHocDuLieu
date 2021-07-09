import pandas as pd
import matplotlib.pyplot as plt

#a. Trực quan hoá dữ liệu theo sơ đồ hình: cột, hình tròn (tính phần trăm) theo sl hoa
xl = pd.ExcelFile('xyz.xlsx')
df = pd.read_excel(xl)
print(df)

#Biểu đồ cột
"""
plt.bar(range(len(df['STT'])),list(df['Số lượng']))
plt.title("Biểu đồ tròn về số lượng hoa")
plt.xlabel("Tên hoa")
plt.ylabel("Số lượng")
plt.xticks(range(len(df['STT'])),df['Tên'])
plt.show()
"""

"""
#Biểu đồ tròn
plt.pie(df['Số lượng'],labels=df['Tên'],autopct='%.2f%%')#auto percentage
plt.title("Biểu đồ tròn về số lượng hoa")
plt.show()
"""

#b.Tính tổng giá tiền các loại hoa
print("Tổng giá tiền các loại hoa")
df['Tổng']=df['Số lượng']*df['Đơn giá']
print(df)
