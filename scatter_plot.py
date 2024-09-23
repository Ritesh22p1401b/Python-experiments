import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,15,20,25,30,35,40])
y=np.array([2,4,6,8,10,12,14])
plt.scatter(x,y,color='red')
x=np.array([10,15,26,28,30,34,40])
y=np.array([2,4,6,9,10,13,15])
plt.scatter(x,y,color='blue')
plt.show()


x=np.array([30,19,15,12])
y=np.array([3,8,14,22])
plt.bar(x,y,label='BMW',width=5)
x1=np.array([40,45,78,89])
y1=np.array([2,5,9,3])
plt.bar(x1,y1,label="Audi",color='r',width=5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (Km)')
plt.title('information')
plt.show()


x=np.array([35,25,15,10])
plt.pie(x)
plt.show()
