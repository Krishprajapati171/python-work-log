sub=[]
for i in range(5):
    k=str(input("Enter the subject names::"))
    print(sub.append(k))
print(sub)

marks=[]
q=0
for i in range(5):
    z=int(input("Enter the marks::"))
    print(marks.append(z))
    q=q+z
print(marks)
print("sum=",q)
print('The average of the  obtained ::',q/5)


if(q>=90 and q<99):
    print('A')

elif(q>=80 and q<=89):
    print('B')

else:
    print('c')