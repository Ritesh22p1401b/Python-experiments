# WAP to print twin prime.

num=1000
# num=int(input("Enter the number upto which
#  you have to find twin prime number"))

for i in range(3,num+1):
    temp = 0
    k=i+2
    for j in range(2,i):
        if i%j == 0 or k%j==0:
            temp=1
            break
    if temp ==0:
        print(i,k)

