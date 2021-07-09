from os import openpty
import numpy as np
import matplotlib.pyplot as mplt
import pandas as pd

file_location = '/Users/duynguyen/Desktop/Python/ontapfilexlxs/xyz.xlsx'
flower = pd.read_excel(file_location)
flower['Tổng'] = flower['Đơn giá'] * flower['Số Lượng']

flower_subset = flower[['Tên','Số Lượng']]
earning_by_subset = flower_subset.pivot_table(index=['Tên'])
earning_by_subset.plot(kind = 'barh')
mplt.ylabel('Số Lượng')
mplt.show()
mplt.pie(flower['Số Lượng'],labels= flower['Tên'], autopct= '%1.1f%%')
mplt.show()
print(flower)
flower.to_excel('/Users/duynguyen/Desktop/Python/ontapfilexlxs/xyzx.xlsx')