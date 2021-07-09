import numpy as np
import matplotlib.pyplot as mp
data = {'Chó':20,'Mèo':10,'Chuột':50,'Heo':100,'Chim':120,'Cá':70}

mp.pie(list(data.values()),labels=list(data.keys()),autopct='%1.1f%%')
mp.title("Thú cưng của tôi")
mp.show()
