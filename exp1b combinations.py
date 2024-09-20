#WAP to find combunation of number 

n=int(input("enter the n number"))
r=int(input("enter the r number"))
#n,r=5,3
dif=n-r

if n>=0 and r==0:
    print("1")

elif n<r:
    print("n should be larger than r")

elif (n>0 and r>0) or n==r:

    n_f=1
    while(n>=1): #(n)!
        n_f=n_f*n
        n-=1

    r_f=1
    while(r>=1): #(r)!
        r_f=r_f*r
        r-=1

    n_r_f=1
    while(dif>=1): # (n-r)!
        n_r_f=n_r_f*dif
        dif-=1

    print((n_f)//((n_r_f)*(r_f)))
