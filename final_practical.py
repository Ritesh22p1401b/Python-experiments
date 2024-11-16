

# num=100

# for i in range(3,num+1):
#     temp=0
#     k=i+2
#     for j in range(2,i):
#         if i%j==0 or k%j==0:
#             temp=1
#             break
#     if temp==0:
#         print(i,k)
      

# import numpy as np
# import matplotlib.pyplot as plt 

# x_axis=np.linspace(-50,50,400)
# y_axis=[x*x for x in x_axis]
# plt.plot(x_axis,y_axis)
# plt.grid()
# plt.show()

# import numpy as np 

# arr=np.array([[12,3,4],[45,89,56],[55,2220,3332]])


# print(f"original array:{arr}")
# col1,col2=0,1


# arr[:,[col1,col2]]=arr[:,[col2,col1]]

# print(arr)

# class Student:

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)


# student=[]

# for i in range(3):
#     name=input("enter the name")
#     age=input("age")


#     s1=Student(name,age)
#     student.append(s1)

# for s in student:
#     s.display()

