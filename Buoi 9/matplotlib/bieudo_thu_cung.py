import numpy as np
import matplotlib.pyplot as plt

data={'Chó':20,'Mèo':10,'Chuột':5,'Heo':100,'Chim':120,'Cá':70}

plt.bar(range(len(data)),list(data.values()))
plt.xticks(range(len(data)),data.keys())
plt.title('Thú cưng của tôi')
plt.show()
