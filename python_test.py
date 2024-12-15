
######  Question-1

# enter 10 element by user in list and if user enter duplicate value in this list
#  but print new list and remove duplicate value from old list.


# l1=[]
# print(type(l1))
#
# for i in range(10):
#     k=l1.append(int(input("Enter the number by user=")))
#     print(l1)
#
#
#
# l2=list(set(l1))
# print(l2)
#
#
# l1=list(set(l2))
# print(l1)





########  Question-2
#  list=[1,2,3,4,5,6,7,8,9,10]
  # print odd and even element of lists using lamada function.
  # ex l1=[1,3,5,7,9]
  #    l2=[2,4,6,8,10]
# l1=[1,2,3,4,5,6,7,8,9,10]
# k=list(map(lambda l1: l1%2==0,l1))
# print("The even numbers from the list:",k)





####### Question-3
# enter tuple like 'python''is''object''oriented''programming''language' output = python is object oriented
# programming language

# t1=('python''is''object''oriented''programming''language')
# print(type(t1))
# print(t1.split())
# print(t1)



####### Question-4

# print sum of 1 to 10 using loop.

# num=int(input("Enter the total number="))
# k=0
# for i in range(num):
#     i=i+1
#     k=k+i
#
#
# print(f"Sum of the total nunmbers entered by the user {num} is = {k}")
#
#
#



###### Question-5

#  IN:{1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'five'}
#   output=op:['One', 1, 'Two', 2, 'Three', 3, 'Four', 4, 'five', 5]


# dict1={1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'five'}
# print(type(dict))
#
# a=dict1.values()
# print(f"The values of the dictionary is={a}")
#
# b=dict1.keys()
# print(f"The keys of the dictionary is = {b}")
#
#
# k=zip(dict1.keys(),dict1.values())
# print(k)
#


####  Question-6
# l=['j','a','v','a','t','p','o','i','n','t']
# output=tnioptavaj

#
# l1=['j','a','v','a' 't','p','o','i','n','t']
# print(type(l1))
# print(l1[::-1])
#





##### Question - 7
##  i)returns a set that contains items that exist in either set, but not in both.
  #ii)returns a set that contains items that exist in the first set but not in the second.


## (i)

# s1={1,2,3,4,5}
# s2={2,5,6,1,9}
#
# k=s1^s2
# print(k)


## (ii)

# s1={1,2,3,4,5,6,7,8}
# s2={5,6,9,10,11,12,14}
# k=s1-s2
# print(k)




#####  Question-8

# IN:1234abcd
#   op:dcba4321
#   using function


# def numbers():
#
#     INPUT="1234abcd"
#     print("input is =",INPUT)
#     print(INPUT[::-1])
# numbers()



##### Question-9

# Pattern:
#   S
#   Sp
#   Spa
#   Spar
#   Spark
#   Sparks
#   SparksT
#   SparksTo
#   SparksToI
#   SparksToId
#   SparksToIde
#   SparksToIdea
#   SparksToIdeas

# n=int(input("Enter the nmumber="))
#
# k="SparksToIdeas"
# for i in range(0,n):
#
#     for j in range(0,i):
#         print(k,end=" ")
#
#     print()





###### Question-10

# enter number by user and when user enter 0 then print total of numbers.
# ex
#    Enter a number: 2
#    Enter a number: 3
#    Enter a number: 4
#    Enter a number: 5
#    Enter a number: 6
#    Enter a number: 6
#    Enter a number: 0
#    total = 26

# k=0
# while  True:
#     n=int(input("Enter the number="))
#     if(n==0):
#         break
#     k=k+n
#
# print("total is =",k)






####### Question-11

# Pattren program
#
# A)16 15 14 13
#   12 11 10 9
#   8  7  6  5
#   4  3  2  1

# num=int(input("Enter the number="))
#   i=i+1
#         print(i,end=" ")
#
#       print()
#
# for i in range(1,num):
#       for j in range(0,i):
#
#

###### Question-12

# list insert by user
#  output =list  according to english caracter for ex output-['are','cat','dog','new', 'see', 'seen']

# l1=[]
#
# for i in range(6):
#    print(l1.append(str(input("Enter the strings for list="))))
#
# print(l1)
#
#

