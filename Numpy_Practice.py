#Question-1

# Array Creation and Initialization
#
# Create a 1D NumPy array containing the first 10 square numbers (0, 1, 4, 9, ..., 81).
# Create a 3x3 NumPy array filled with random integers between 1 and 100.


import numpy as np
import random
# arr=np.array([0,1,2,3,4,5,6,7,8,9])
# z=list(map(lambda arr:arr*arr,arr))
# print("The squaring of the first 10 numbers::",z)
# arr1=np.random.randint(0,101,size=(3,3))
# print(arr1)



# Question-2

# Indexing and Slicing
#
# Given the array arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]]), extract the elements in the second column.
# Extract the last row of the array arr.


# import numpy as np
# arr=np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# print(arr)
# print("Extraction of the element in the second column::",arr[:,1])
# print("Extraction of the last row of the array::",arr[2,:])




#Question-3

# Basic Array Operations
#
# Create two NumPy arrays: a = np.array([1, 2, 3]) and b = np.array([4, 5, 6]). Perform element-wise addition and
# subtraction.
# Create a 3x3 array filled with random integers between 1 and 50, and find the mean of the array.

# import numpy as np
# import random
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# add=arr1+arr2
# print("Addition element-wise:",add)
# sub=arr2-arr1
# print('Subraction element-wise:',sub)
#
# random_Array=np.random.randint(1,50,size=(3,3))
# print("The random array::",random_Array)
# min_Array=np.mean(random_Array)
# print("The mean of the 3*3 matrix is ::",min_Array)




#Question-4

# Reshaping Arrays
#
# Reshape the array arr = np.array([1, 2, 3, 4, 5, 6]) into a 2x3 matrix.
# Flatten the 2D array arr back into a 1D array.

# import  numpy as np
#
# arr=np.array([1,2,3,4,5,6])
# reshaping_array=arr.reshape(2,3)
# print("The reshaping of the given araay is::",reshaping_array)
# new_array=reshaping_array.flatten()
# print("Flatten of the 2D array back into 1D array::",new_array)




#Question-5

# Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.

# import  numpy as np
#
# arr=np.zeros(10)
# print(arr)
# arr1=np.ones(10)
# print(arr1)
# arr2=np.full((3,3),5)
# print(arr2)


# #Question-6
#  Write a NumPy program to compute the multiplication of two given matrixes.

# import numpy as np
# arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# arr2=np.array([[10,11,12],[13,14,15],[16,17,18]])
# ans=np.matmul(arr1,arr2)
# print("The multiplication of the two matrices is::",ans)



# Question=7
# Write a NumPy program that creates a large 1D array and write a function to calculate the sum of its elements
# using a for loop.
# Then, optimize it using NumPy's built-in functions.


# import  numpy as np
# import random
#
# large_array = np.random.rand(1_000_000)
#
# def sum_of_large_array():
#     total=0
#     for i in large_array:
#         total=total+i
#     print("Sum using the loop:;",total)
# sum_of_large_array()
#
#
# arr=np.sum(large_array)
# print("sum using the in-built method::",arr)


#Question-8

# 1. Write a NumPy program to sort a given array of shape 2 along the first axis, last axis and on flattened array.
# Expected Output:
# Original array:
# [[10 40]
# [30 20]]
# Sort the array along the first axis:
# [[10 20]
# [30 40]]
# Sort the array along the last axis:
# [[10 40]
# [20 30]]
# Sort the flattened array:
# [10 20 30 40]



# import numpy as np

# a = np.array([[10, 40], [30, 20]])
# print("Original array:")
# print(a)
# print("Sort the array along the first axis:")
# print(np.sort(a, axis=0))
# print("Sort the array along the last axis:")
# print(np.sort(a))
# print("Sort the flattened array:")
# print(np.sort(a, axis=None))