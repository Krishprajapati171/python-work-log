import pandas as pd

# Question 1
# Write a Pandas program to create and display  a one-dimensional array-like object containing an array of data using
# Pandas module.



# import pandas as pd
# import numpy as np
#
# arr1=np.array(["krish","Dhruv","Shiva","Patel"])
# z=pd.Series(arr1)
# print(z)



# Question 2
 # Write a Pandas program to convert a Panda module Series to Python list and it's type.


# import  pandas as pd
#
# arr1=pd.Series(['krish','shiva','dhruv','patel'])
# print(arr1)
# z=list(arr1)
# print("into the list::",z)



# Question 3
# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]


# import  pandas as pd
#
# s1=[2,4,6,8,10]
# s2=[1,3,5,7,9]
#
# series1=pd.Series(s1)
# series2=pd.Series(s2)
#
# add=series1+series2
# print("add of the both series=",add)
#
# sub=series2-series1
# print("subraction of both series=",sub)
#
# mul=series1*series2
# print("Multiplication of the both series=",mul)
#
# div=series1/series2
# print("Division of the both series=",div)


#Question-4

# . Write a Pandas program to convert a dictionary to a Pandas series.

# Sample Series:
# Original dictionary:
# {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
#
# Converted series:
# a    100
# b    200
# c    300
# d    400
# e    800
# dtype: int64

# import pandas as pd
#
# dictionary={  'a':100,  'b':200,   'c':300, 'd':400,   'e':800 }
#
# series=pd.Series(dictionary)
# print("Into dictionary:",series)


# Question-5
# Write a Pandas program to change the data type of given a column or a Series.
#
# Sample Series:
#     Original Data Series:
# 0       100
# 1       200
# 2    python
# 3    300.12
# 4       400
# dtype: object

# Change the said data type to numeric:
# 0    100.00
# 1    200.00
# 2       NaN
# 3    300.12
# 4    400.00
# dtype: float64


# import pandas as pd
#
# s1=pd.Series([100,200,'python',300.12,400])
# print("The normal given:",s1)
#
# z=pd.to_numeric(s1,errors='coerce')
# print("By changing its data type::",z)


#Question-6
# Write a Pandas program to convert the first column of a DataFrame as a Series.

# Original DataFrame
#    col1  col2  col3
# 0     1     4     7
# 1     2     5     5
# 2     3     6     8
# 3     4     9    12
# 4     7     5     1
# 5    11     0    11
#
# 1st column as a Series:
# 0     1
# 1     2
# 2     3
# 3     4
# 4     7
# 5    11
# Name: col1, dtype: int64
# <class 'pandas.core.series.Series'>


# import  pandas as pd
#
# df=pd.DataFrame({
#     'col1':[1,2,3,4,7,11],
#     'col2':[4,5,6,9,5,0],
#     'col3':[7,5,8,12,1,11]
# })
#
#
# print('The given solution::',df['col1'])


#question-7

#  Write a Pandas program to display the default index and set a column as an Index in a given dataframe.
# Test Data:
#
# 0        s001     V  Alberto Franco     15/05/2002      35  street1   t1
# 1        s002     V    Gino Mcneill     17/05/2002      32  street2   t2
# 2        s003    VI     Ryan Parkes     16/02/1999      33  street3   t3
# 3        s001    VI    Eesha Hinton     25/09/1998      30  street1   t4
# 4        s002     V    Gino Mcneill     11/05/2002      31  street2   t5
# 5        s004    VI    David Parkes     15/09/1997      32  street4   t6




# import pandas as pd

# df=pd.DataFrame(
#     {
#         'index':[0,1,2,3,4,5],
#         'Enroll_no':['s001','s002','s003','s004','s005','s006'],
#         'class':['v','v','VI','VI','V','VI'],
#         'Name':['Alberto Franco','Gino Mcneill','Ryan Parkes','Eesha Hinton','Gino Mcneill','David Parkes'],
#         'D.O.B':['15/05/2002 ','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
#         'Unique_no':[35,32,33,30,31,32],
#         'Address':['street1','street2','street3','street1','street2','street4'],
#         't_id':['t1','t2','t3','t4','t5','t6']
#     }
# )
#
# print(df.head(10))
# print(df.tail(2))


#Question-8

#  Write a Pandas program to display the dimensions or shape of the World alcohol consumption dataset. Also extract the
#  column names from the dataset.
# Test Data:
#
#    Year       WHO region                Country Beverage Types  Display Value
# 0  1986  Western Pacific               Viet Nam           Wine           0.00
# 1  1986         Americas                Uruguay          Other           0.50
# 2  1985           Africa           Cte d'Ivoire           Wine           1.62
# 3  1986         Americas               Colombia           Beer           4.27
# 4  1987         Americas  Saint Kitts and Nevis           Beer           1.98


# df=pd.read_csv("world_alcohol.csv")
#
# print("The data of first 10:::")
# print(df.head(10))
#
# print("The data of last 10::::")
# print(df.tail(10))
#
# print("THE SHAPE OF THE SOURCE::",df.shape)
# print("THE DIMENSIONS OF THE SOURCE::",df.ndim)




