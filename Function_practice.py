# Exercise 1: Create a function in Python
# Write a program to create a function that takes two arguments, name and age, and print their value.



# def info(name,age):
#     print(f"Your name is {name}and tell your age {age}")
#
# info("john",17)







# Exercise 2: Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.

# Note: Create a function in such a way that we can pass any number of arguments to this function, and
# the function should process them and display each argument’s value.



# def func1(*nums):        # variable-length arguments..
#     z=0
#     for i in nums:
#
#         z=z+i
#     print(z)
# func1(10,10)
# func1(20,30)
# func1(1,1,1)





# Exercise 3: Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and
# subtraction. Also, it must return both addition and subtraction in a single return call.

# Given
# def calculation(a, b):
#     # Your Code
#
# res = calculation(40, 10)
# print(res)




# def calculation(a,b):
#     return a+b,a-b
#
# res=calculation(40,10)
# print(res)




# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.
#
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary


# Given:
#
# showEmployee("Ben", 12000)
# showEmployee("Jessa")



# def show_employee(name,salary=9000):
#     print(f"employee name is :: {name}")
#     print(f"salary is {salary}")
#
# show_employee("Ben",12000)
# show_employee("Jessa")




# Exercise 5: Create an inner function to calculate the addition in the following way
#
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it




# def func1(a,b):
#     q=a**b
#
#     def add(a,b):
#         return a+b
#     k=add(10,20)
#
#     return k+5
# result=func1(1,1)
# print(result)




# Exercise 6: Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
#
# A recursive function is a function that calls itself again and again.
#
# Expected Output:
# 55




# z=0
# def sum_of_nums(nums):
#     if nums:
#         return nums+sum_of_nums(nums-1)
#     else:
#         return 0
# result=sum_of_nums(10)
# print(result)



# # Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
# Given:

# def display_student(name, age):
#     print(name, age)
#
# display_student("Emma", 26)




# def display_student(name,age):
#     print(f"Your name:{name}",f"age is {age}")
#
# display_student("Emma",26)
# display_student("Taylor",17)




# Exercise 8: Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]
# Expected Output:
# 24


# def largest_of_nums():
#     x=[4,6,8,24,12,2]
#     print(max(x))
# largest_of_nums()


