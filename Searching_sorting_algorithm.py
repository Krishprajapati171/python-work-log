#####Linear Search#####

# class linear:
#
#     def linear_search(self):
#         n = int(input("Enter the number="))
#         l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         for i in range(0, n):
#             if (l1[i] == n):
#                 print(f"it is found  in the list at location  {i} ")
#                 break
#
# l=linear()
# l.linear_search()

# Time complexity
 # Best case: 0(1)
 #Avg case: 0(n)
 #worst case:0(n)


#####Binary Search#####

# def Binary_search():
#   l1=[]
#   print(type(l1))
#
#   for n in range(10):
#     l1.append(int(input("enter the number")))
#     print(l1)
#
#
#   key_element=int(input("Enter the key element to search  from list(l1)="))
#   print(f"The key_element is ={key_element}")
#
#   low=0
#   high=len(l1)-1
#
#   while(low<=high):
#
#     mid=(low+high)/2
#     if( l1[mid]==key_element):
#          return mid
#     elif(l1[mid]<=key_element):
#           low=mid+1
#     else:
#           high=mid-1
#
# Binary_search()

# Time complexity
 # Best case: 0(1)
 #Avg case: 0(log n)
 #worst case:0(log n)


#####Bubble Sort#####

# def bubble_sort():
#   l1=[]
#   print(type(l1))
#
#   for  n in range(10):
#      l1.append(int(input("Enter the number=")))
#      print(l1)
#
#
#      for  i in range(n-1):
#       for j in range(0,n-i-1):
#         if(l1[j]>l1[j+1]):
#           temp=l1[j]
#           l1[j]=l1[j+1]
#           l1[j+1]=temp
#           print(l1)
#
# bubble_sort()


# Time complexity
 # Best case: 0(n)
 #Avg case: 0(n^2)
 #worst case:0(n^2)

#####Selection Sort#####

# def selection_sort():
#     l1=[]
#
#     for n in range(10):
#         print(l1.append(int(input("Enter the numbers in list="))))
#
#     for i  in  range(len(l1)):
#         min=i
#
#         for j in range(i+1,len(l1)):
#
#             if(l1[j]<l1[min]):
#                 min=j
#             l1[i], l1[min] = l1[min], l1[i]
#             print(l1)
# selection_sort()


# Time complexity
 # Best case: 0(n^2)
 #Avg case: 0(n^2)
 #worst case:0(n^2)

#####Insertion Sort#####

# a = []
# n=int(input("Enter the size of the array"))
# print("Enter the elements of array")
# for i in range(n):
#   a.append(int(input("Enter element:")))
# for i in range (1,n):
#   j=i-1
#   x=a[i]
#   while j>-1 and x<a[j]:
#     a[j+1]=a[j]
#     j=j-1
#   a[j+1]=x
# print(a)

# Time complexity
 # Best case: 0(n)
 #Avg case: 0(n^2)
 #worst case:0(n^2)


#####Quick Sort#####

# def partition(arr,low,high):
#   i=low+1
#   pivot=arr[low]
#   j=high
#   while i<=j:
#     while arr[i]<=pivot and i<len(arr):
#       i+=1
#     while arr[j]>pivot and j>0:
#       j-=1
#     if i<j:
#       arr[i],arr[j]=arr[j],arr[i]
#   arr[low],arr[j]=arr[j],arr[low]
#   return j
# def quicksort(arr,low,high):
#   if low<high:
#     m=partition(arr,low,high)
#     quicksort(arr,low,m-1)
#     quicksort(arr,m+1,high)
# n=int(input("Enter the number of elements:"))
# arr =[]
# low=0
# high=n-1
# print("Enter the elements of array")
# for i in range(n):
#   arr.append(int(input()))
#
# print("Sorted array is")
# quicksort(arr,0,n-1)
# print(arr)

# Time complexity
 # Best case: 0(n log n)
 #Avg case: 0(n log n)
 #worst case:0(n^2)






# #####Merge Sort#####
#
#
# def merge_sort(arr):
#
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
#
#
#     left_sorted = merge_sort(left_half)
#     right_sorted = merge_sort(right_half)
#
#
#     return merge(left_sorted, right_sorted)
#
#
# def merge(left, right):
#     merged = []
#     i = j = 0
#
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
#
#
#     while i < len(left):
#         merged.append(left[i])
#         i += 1
#     while j < len(right):
#         merged.append(right[j])
#         j += 1
#
#     return merged
#
#
# if __name__ == "__main__":
#     arr = [38, 27, 43, 3, 9, 82, 10]
#     print("Original Array:", arr)
#     sorted_arr = merge_sort(arr)
#     print("Sorted Array:", sorted_arr)

# Time complexity
 # Best case: 0(n log n)
 #Avg case: 0(n log n)
 #worst case:0(n long n)
