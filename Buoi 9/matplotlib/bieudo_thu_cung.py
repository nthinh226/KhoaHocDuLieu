import numpy as np
import matplotlib.pyplot as plt

data={'Chó':20,'Mèo':10,'Chuột':5,'Heo':100,'Chim':120,'Cá':70}
data1={'Chó':3,'Mèo':25,'Chuột':5,'Heo':6,'Chim':2,'Cá':2}
plt.bar(range(len(data)),list(data.values()), label='1')
plt.bar(range(len(data1)),list(data1.values()), label='2')
plt.xticks(range(len(data)),data.keys())
plt.title('Thú cưng của tôi')
plt.legend()
plt.show()
