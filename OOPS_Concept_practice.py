# Question-1
#  Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

# import  random
#
# pi = 3.14
# radius = float(input("Enter the value of radius::"))
# class Circle:
#     def area_of_circle(self):
#         x=pi*radius*radius
#         print("The area of the circle:",x)
#
#     def perimeter_of_circle(self):
#         z=2*pi*radius
#         print("The perimeter of the circle",z)
#
#
# c=Circle()
# c.area_of_circle()
# c.perimeter_of_circle()



# # Question-2
# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.


# import math
# num1=int(input("Enter the value of num1::"))
# num2=int(input("Enter the value of num2::"))
#
# class calculator:
#
#     def addition(self):
#         z=num1+num2
#         print("The addition of the given::",z)
#
#     def subtraction(self):
#         x=num2-num1
#         print("The subtraction of the given::",x)
#
#     def multiplication(self):
#         c=num1*num2
#         print("The multiplication of the given::",c)
#
#     def division(self):
#         v=num1/num2
#         print("The Division of the given::",v)
#
#     def square_root(self):
#         b=math.sqrt(num1)
#         print("The Square root of the given::",b)
#
#     def floor_division(self):
#         n=num1//num2
#         print("The floor divsion of the given::",n)
#
#     def percentage(self):
#         m=num1%num2
#         print("The percentage of the given::",m)
#
# c=calculator()
# c.addition()
# c.division()
# c.subtraction()
# c.percentage()
# c.square_root()
# c.multiplication()
# c.floor_division()



# Question-3
#Gadget Hierarchy
# Create a base class Gadget with:
# Attributes: brand and price.
# Method: info() to print the brand and price.
# Create child classes:
# Smartphone with an additional attribute OS (e.g., Android, iOS), and override info() to include the OS.
# Laptop with an additional attribute RAM and override info() to include the RAM size.


# class Gadget:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#
#     def info(self):
#         print(f"The  brand is {self.brand} and {self.price}")
#
#
#
# class Smartphone(Gadget):
#     def __init__(self,brand,price,os):
#         super().__init__(brand,price)    # use of super keyword
#         self.os=os
#
#     def info(self):
#         print(f"The brand is {self.brand} and {self.price} with os as {self.os}")
#
#
# class Laptop(Gadget):
#     def __init__(self,brand,price,ram):
#         super().__init__(brand,price)   # use of super keyword
#         self.ram=ram
#
#     def info(self):
#         print(f"The brand is {self.brand}, price is {self.price} with having {self.ram}")

# s=Smartphone("Samsung s24 ultra",9999999,"android")
# l=Laptop("Lenevo",85000,"12GB")
# s.info()
# l.info()




#Question-4

# Create a class Student that abstracts a student. Each student should have:
#
# name (string)
# roll_number (int)
# marks (dictionary with subject names as keys and scores as values)
# The class should provide the following methods:
#
# A constructor to initialize all attributes.
# A method add_subject(subject, score) to add a new subject and its score to the marks.
# A method get_average() to calculate and return the average marks of the student.
# A method display_details() to display the student's details (name, roll number, and marks).
# Write a program to create a Student object, add some subjects, display the details, and calculate the average marks.
#




# from abc import ABC, abstractmethod
#
# class StudentBase(ABC):
#     @abstractmethod
#     def add_subject(self, subject, score):
#
#         pass
#
#     @abstractmethod
#     def get_average(self):
#         pass
#
#     @abstractmethod
#     def display_details(self):
#
#         pass
#
#
# class Student(StudentBase):
#     def __init__(self, name, roll_number):
#
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = {}
#
#     def add_subject(self, subject, score):
#
#         self.marks[subject] = score
#
#     def get_average(self):
#
#         if not self.marks:
#             return 0
#         total_marks = sum(self.marks.values())
#         num_subjects = len(self.marks)
#         return total_marks / num_subjects
#
#     def display_details(self):
#
#         print(f"Student Name: {self.name}")
#         print(f"Roll Number: {self.roll_number}")
#         print("Marks:")
#         for subject, score in self.marks.items():
#             print(f"  {subject}: {score}")
#         print(f"Average Marks: {self.get_average():.2f}")
#
#
#
# student = Student("krish", 171)
#
#
# student.add_subject("Math", 92)
# student.add_subject("Physics", 88)
# student.add_subject("Chemistry", 81)
#
#
# student.display_details()
#
#
# average = student.get_average()
# print(f"Calculated Average Marks: {average:.2f}")


# Question 5

# Constructor Overriding
#
# Create a base class Person with an __init__ method that takes name and age.
# Create a derived class Student that overrides the __init__ method to include an additional parameter student_id.
# Ensure that the Student class calls the constructor of the Person class.
# Instantiate a Student object and print its attributes.

# class person:
#     def __int__(self,name,age):
#         self.name=name
#         self.age=age
#
#
# class student(person):
#     def __init__(self, name, age, student_id):
#         super().__int__(name ,age)
#         self.student_id=student_id
#
#     def display(self):
#         print(f"Name is {self.name} and age is {self.age} with student id as {self.student_id}")
#
# p=person()
# s=student("krish",21,171)
# s.display()


