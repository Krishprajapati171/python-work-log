"""Write a program that takes a list of numbers and returns the sum of all the elements."""

l1=[]
l2=[]
q=0
for i in range(5):
    k=int(input("Enter your values::"))
    l1.append(k)
    q=q+l1[i]
print(l1)
print("sum is::",q)

x=0
for j in range(5):
    z=int(input("Enter your values::"))
    l2.append(z)
    x=x+l2[j]
print(l2)
print("Sum is =",x)


