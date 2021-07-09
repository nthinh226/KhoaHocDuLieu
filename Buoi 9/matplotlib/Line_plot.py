import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0.,8.,0.2)
#y=x^2
#y=x^3
#y=x^4
plt.plot(x,x**2,'r^',x,x**3,'bp',x,x**4,'g*')
plt.show()
