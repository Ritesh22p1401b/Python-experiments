
# WAP to create a pie chart by using two list data

import matplotlib.pyplot as plt
list1=[10,5,5,6,4,12,8]
list2=[15,2.5,2.5,10,20]
list=list1+list2
label=["A","B","C","D","E","F","G","H","I","J","K","L"]
color=['r','c','b','g','m','g','y','r','m','c','g','b']
plt.pie(
    list,labels=label,colors=color,
    explode=(0,0,0,0,0,0,0,0,0,0,0,0.1),
    startangle=90,shadow=True,autopct='%1.f%%'
)
plt.legend(loc='upper right')
plt.title('Market share of clothing brand')
plt.show()
