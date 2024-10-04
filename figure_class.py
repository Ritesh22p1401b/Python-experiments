

import matplotlib.pyplot as plt 

fig = plt.figure(figsize=(6,2), dpi=100, facecolor='blue')
ax=fig.add_subplot(121)
ay=fig.add_subplot(122)
ax.plot([12,56,78],[100,200,300])
ay.plot([1,6,11],[100,200,300])
ax.set_title("figure plot")
ax.set_xlabel("x axis")
ax.set_label("y axis")
ay.set_title("figure plot")
ay.set_xlabel("x axis")
ay.set_label("y axis")
plt.show()

