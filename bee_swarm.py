
import matplotlib.pyplot as plt
import seaborn
tip = seaborn.load_dataset("tips")
plt.figure(figsize=(8, 6))  
seaborn.swarmplot(x='day', y='total_bill', data=tip)
plt.title('Bee Swarm Plot of Total Bill by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.show()




