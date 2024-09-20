import matplotlib.pyplot as plt
import numpy as np
x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])
font1={'family':'serif','color':'red','size':5}
font2={'family':'serif','color':'blue','size':5}
plt.subplot(2,3,1)
plt.plot(x,y)
plt.title("name1")

plt.title("sport watch data",fontdict=font1)
plt.xlabel("average pulse",fontdict=font2)
plt.ylabel("calorie buranage",fontdict=font2)
plt.legend(['single element'])
plt.grid(axis='x')

x1=np.array([10,20,30,40,50])
y1=np.array([1,2,3,4,5])
plt.subplot(2,3,2)
plt.plot(x1,y1)
plt.title("name2")

x2=np.array([10,20,30,40,50])
y2=np.array([1,2,3,4,5])
plt.subplot(2,3,3)
plt.plot(x2,y2)
plt.title("name3")


x3=np.array([10,20,30,40,50])
y3=np.array([1,2,3,4,5])
plt.subplot(2,3,4)
plt.plot(x3,y3)
plt.title("name4")


x4=np.array([10,20,30,40,50])
y4=np.array([1,2,3,4,5])
plt.subplot(2,3,5)
plt.plot(x4,y4)
plt.title("name5")

x5=np.array([10,20,30,40,50])
y5=np.array([1,2,3,4,5])
plt.subplot(2,3,6)
plt.plot(x5,y5)
plt.suptitle('name')
plt.show()

