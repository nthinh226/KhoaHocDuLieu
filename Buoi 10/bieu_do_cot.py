import numpy as np
#thêm bộ thư viện matplot với tên viết tắt plt
import matplotlib.pyplot as plt

data={'Cam':50,'Xoài':75,'Mít':500,'Ổi':192,'Vải':178,'Táo':300,'Lê':200}

plt.bar(range(len(data)),list(data.values()),label="Trái cây",color="r")
plt.legend()
plt.xticks(range(len(data)),data.keys())
plt.ylabel("Số lượng")
plt.title("Biểu đồ số lượng các loại trái cây")
plt.show()
