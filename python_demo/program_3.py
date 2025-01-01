# l1=[]
# n=int(input("Enter the value:"))
#
# for i in range(n):
#     z=int(input("Enter the elements::"))
#     l1.append(z)
#     l1.reverse()
#     print(l1)
#     print(l1.sort())


l1=[]


n=int(input("Enter the value::"))

for i in range(n):
    z=int(input("Enter the elements::"))
    l1.append(z)
print(l1)




#revserse order
for k in range(0,n):
        for j in range(0,n-1):
            if(l1[j]>l1[j+1]):
                l1[j],l1[j+1]=l1[j+1],l1[j]

print("1st=",l1)



for k in range(0,n):
        for j in range(0,n-1):
            if(l1[j]<l1[j+1]):
                l1[j],l1[j+1]=l1[j+1],l1[j]

print("2nd=",l1)



