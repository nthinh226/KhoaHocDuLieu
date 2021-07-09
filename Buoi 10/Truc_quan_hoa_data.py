import numpy as np
import matplotlib.pyplot as plt
data={'Cam':50,'Xoài':75,'Mít':500,'Ổi':192,'Vải':178,'Táo':300,'Lê':200}

plt.bar(range(len(data)),list(data.values()),label="Số lượng",color="r")
plt.legend()
plt.xticks(range(len(data)),data.keys())
plt.xlabel("Loại trái cây")
plt.ylabel("Số lượng")
plt.title('Biểu đồ số lượng trái cây')
plt.show()
