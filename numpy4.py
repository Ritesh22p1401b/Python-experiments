import numpy as np



arr_1=np.array([1,5,6,78,9])
arr_2=np.array([45,5,1,78,45])



print(np.union1d(arr_1,arr_2))
print(np.intersect1d(arr_1,arr_2))
print(np.setdiff1d(arr_1,arr_2))


