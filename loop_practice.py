# Python if else, for loop, and range() Exercises


# Exercise 1: Print first 10 natural numbers using while loop

# num=int(input("Enter the number:"))
# i=0
# while(i<=num):
#     i=i+1
#     print("The first 10 natural number::",i)
#



# Exercise 2: Print the following pattern

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *


# n=int(input("Enter the n::"))
#
# for i in range(0,n):            #rows
#     for j in range(0,i+1):      #columns
#         print("*",end=" ")
#
#     print()



# Exercise 3: Calculate sum of all numbers from 1 to a given number


# num=int(input("Enter the number::::"))
#
# z=0
# for i in range(0,num):
#     i=i+1
#     z=z+i
# print("The sum  of the given sum of all numbers from 1 to a given number::",z)



# Exercise 4: Print multiplication table of a given number

# n=int(input("Enter the value of n::"))
#
# for i in range(1, 11, 1):
#
#     product = n * i
#     print(product)
#



# Exercise 5: Display numbers from a list using a loop

# numbers = [12, 75, 150, 180, 145, 525, 50]

# Write a Python program to display only those numbers from a list that satisfy the following conditions:

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop

# numbers=[12,75,150,180,145,525,50]
#
# for i in range(len(numbers)):
#     if(numbers[i]>=150):
#         continue
#     elif(numbers[i]>=500):
#         break
#     print(i)





# Exercise 6: Count the total number of digits in a number

# Write a Python program to count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5.


# num = 75869
# count = 0
# while num != 0:
#     num = num // 10
#     count = count + 1
# print("Total digits are:", count)





# Exercise 7: Print the following pattern
# Write a Python program to print the reverse number pattern using a for loop.
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1



# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()





# Exercise 8: Print list in reverse order using a loop

# Given list1 = [10, 20, 30, 40, 50]


# list1=[10,20,30,40,50]
# z=reversed(list1)
# for i in z:
#
#     print(i)





# Exercise 9: Display numbers from -10 to -1 using for loop


# num=-10
#
# while(num<=-1):
#     print(num)
#     num=num+1
#




# Exercise 11: Find the sum of the series up to n terms
# Write a program to calculate the sum of series up to n terms. For example, if n = 5
# the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

# Given:
# # number of terms
# n = 5


# n = 5

# start = 2
# sum_seq = 0
#
# for i in range(0, n):
#     print(start, end="+")
#     sum_seq += start
#     start = start * 10 + 2
# print("\nSum of above series is:", sum_seq)


# Exercise 12: Print the following pattern
# Write a program to print the following start pattern using the for loop

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *




# rows=int(input("Enter the number of the rows::"))
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")
#
# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")