import matplotlib.pyplot as plt

# x=[10,20,30,40,50]
# plt.boxplot(x,notch=True)
# plt.show()


x=[10,20,30,40,50]
plt.boxplot(x,vert=False,widths=0.5,labels=["python"],patch_artist=True,showmeans=True)
plt.show()




