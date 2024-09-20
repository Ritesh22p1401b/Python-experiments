l1=[]
#print("Enter the list element")
for i in range(7):
    l1.append(int(input("Enter the element")))
print(l1)

print(l1[0:5]) #slicing
print(l1[-1])
print(l1[2:])

l1.insert(2,54) # insert
l1.insert(0,89)
print(l1)

l1.sort() #sorting
print(l1)

l4=[1,2,3,6,99,100] #extend
l1.extend(l4)
print(l1)

l1.reverse() #reversing
print(l1)

l=len(l1) #finding length
print(l)

l2=[] #copying list
l2=l1
print(l2)

l1.pop() #poping list
print(l1)


l4=[]
for k in l1:
    l4.append(k)
print(l4)
