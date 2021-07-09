#giả sử có 2 biểu đồ có giá trị
#BT1=([1,4,6,8,3],[11,15,3,10,9])
#BT2=([21,41,16,28,33],[41,25,31,12,19])
#vẽ biểu đồ để ghép 2 biểu đồ thành 1 biểu đồ



import matplotlib.pyplot as plt
plt.bar([1,4,6,8,3],[11,15,3,10,9], label ='BT1')
plt.bar([21,41,16,28,33],[41,25,31,12,19], label ='BT2', color='r')
plt.legend()
plt.xlabel('Cột số')
plt.ylabel('Cột chiều cao')
plt.title('KẾT NỐI 2 BIỂU ĐỒ')
plt.show()
