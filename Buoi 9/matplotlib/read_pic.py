import matplotlib.pyplot as plt
import matplotlib.image as Ima

image=Ima.imread("abc.jpg")
image1=Ima.imread("e8yeshti7la21.jpg")

plt.imshow(image)
plt.show()

"""
fig,axs=plt.subplots(2,2,figsize=(8,8))
axs[0,0].imshow(image)
axs[0,1].imshow(image1)

#luu file
plt.savefig('a.png')
plt.savefig('a.pdf')

plt.show();
"""
