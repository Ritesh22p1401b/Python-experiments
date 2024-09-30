
import matplotlib.pyplot as plt

slices=[12.30,11.40,14.90,7.4,41.60]

labels=['Tata Motors','Mahindra & Mahindra',
    'Hyundai Motor Company','Other Manufacturers','Maruti Suzuki']

colors=['g','r','b','c','b']


plt.pie(slices,labels=labels,colors=colors,
    startangle=90,shadow=True,explode=(0,0,0,0,0.05),autopct='%1.f%%')

plt.legend(loc='upper right')
plt.title('Market Share in Four wheeler Manufacturing')
plt.show()


