
"""
import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4],[1,4,9,16])
plt.title("First Plot")
plt.xlabel("X label")
plt.ylabel("Y lable")
plt.show()
"""
"""
#Biểu đồ cột
import matplotlib.pyplot as plt
import numpy as np

d = ["Cột 1", "Cột 2", "Cột 3"]
d_avg = [5,3,12]
d_avg2 = [4,68,2]

plt.bar(d,d_avg,label="Bar 01")
plt.bar(d,d_avg2,label="Bar 02")
plt.title("Do thi cot")
plt.xlabel("Name")
plt.ylabel("Number")

plt.legend()

plt.show()
"""

"""
#Biểu đồ thú cưng
import numpy as np
import matplotlib.pyplot as plt

data={'Chó':20,'Mèo':10,'Chuột':5,'Heo':100,'Chim':120,'Cá':70}

plt.bar(range(len(data)),list(data.values()),label="A")
plt.xticks(range(len(data)),data.values())
plt.legend()
plt.show()
"""
