def binhphuong(x):
    return x*x
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = list(map (binhphuong, li))
print (squaredNumbers)
