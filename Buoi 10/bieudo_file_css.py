import pandas as pd
import matplotlib.pyplot as plt;

data=pd.read_csv("data.csv", sep=";")

colName=['San luong','Ten']
visualData=data[colName]
visualData=visualData.set_index('Ten')
visualData.plot.pie(y='San luong', figsize=(5, 5))
