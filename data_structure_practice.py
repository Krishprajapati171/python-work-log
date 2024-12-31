# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from
# the list l1 and even index elements from the list l2.

# Given:
#
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]


# list1 = [3, 6, 9, 12, 15, 18, 21]
# list2 = [4, 8, 12, 16, 20, 24, 28]
# res = list()
#
# odd_elements = list1[1::2]
# print("Element at odd-index positions from list one")
# print(odd_elements)
#
# even_elements = list2[0::2]
# print("Element at even-index positions from list two")
# print(even_elements)
#
# print("Printing Final third list")
# res.extend(odd_elements)
# res.extend(even_elements)
# print(res)







# Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
#
# Given:
# list1 = [54, 44, 27, 79, 91, 41]


# list1=[54,44,27,79,91,41]
#
# print(list1.pop(4))
# print("After removing an element from the 4th index::",list1)
#
# res=list1.insert(2,91)
# print(res)
# print("Adding an element at the 2nd index by inserting as ::",list1)
#
# res1=list1.append(89)
# print("At the last i added an element as::",list1)





# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
# Given:
#
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Expected Outcome:
#
# Chunk  1 [11, 45, 8]
# After reversing it  [8, 45, 11]
# Chunk  2 [23, 14, 12]
# After reversing it  [12, 14, 23]
# Chunk  3 [78, 45, 89]
# After reversing it  [89, 45, 78]



# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# print("Original list ", sample_list)
#
# length = len(sample_list)
# chunk_size = int(length / 3)
# start = 0
# end = chunk_size
#
# for i in range(3):
#
#     indexes = slice(start, end)
#
#
#     list_chunk = sample_list[indexes]
#     print("Chunk ", i, list_chunk)
#
#
#     print("After reversing it ", list(reversed(list_chunk)))
#
#     start = end
#     end += chunk_size




#Exercise 4: Count the occurrence of each element from a list
# Write a program to iterate a given list and count the occurrence of each element and create a
# dictionary to show the count of each element

# Given:
#
#
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Expected Output:

# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}




# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# print("Original list ", sample_list)
#
# count_dict = dict()
# for item in sample_list:
#     if item in count_dict:
#         count_dict[item] += 1
#     else:
#         count_dict[item] = 1
#
# print("Printing count of each item  ", count_dict)





# Exercise 5: Create a Python set such that it shows the element from both lists in a pair
# Given:
#
# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]



# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
# s=set()
# print(list(zip(first_list,second_list)))     #use of the zip keyword.....






# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
#
# Given:
#
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}



#
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
#
# new_set=first_set.intersection(second_set)
# print("The common on the both sets ::",new_set)
#
# for i in new_set:
#     first_set.remove(i)
#
# print("First set after removing common element",first_set)





# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
# Given:
#
# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}




# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}
#
#
# if first_set.issubset(second_set):
#     print(True)
#     print(first_set.clear())
#     print(first_set)
#
# elif first_set.issuperset(second_set):
#     print(False)
#     print(second_set.clear())
#     print(second_set)




# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary.
# If not, delete it from the list
# Given:

# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}


# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
#
# print("List:", roll_number)
# print("Dictionary:", sample_dict)
#
#
# roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
# print("after removing unwanted elements from list:", roll_number)




# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
# Given:
#
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}



# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
#
# print(speed.values())
# print("Here is the all values from the dictionary without duplicates::",list(speed.values()))





# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
# Given:
#
# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# Expected Outcome:
#
# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41
# max: 99





# sample_list = [87, 52, 44, 53, 54, 87, 52, 53]
#
# print("Original list", sample_list)
#
# sample_list = list(set(sample_list))
# print("unique list", sample_list)
#
# t = tuple(sample_list)
# print("tuple ", t)
#
# print("Minimum number is: ", min(t))
# print("Maximum number is: ", max(t))