import matplotlib.pyplot as plt
import numpy as np

x=np.array([15,30,50,60,75,90])
y=np.array([25,50,75,100,125,150])

plt.bar(x,y,width=3,label='Indigo')

a=np.array([9,18,27,36,45,54])
b=np.array([8,16,24,32,40,48])
plt.bar(a,b,label='Air India',width=3,color='r')

plt.legend()
plt.xlabel('Days')
plt.ylabel('Flight Hours (Hrs)')
plt.title('Flight Data')
plt.show()


