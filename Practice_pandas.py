# Exercise 1: From the given dataset print the first and last five rows
# Expected Output:
#
# # Python Pandas printing first 5 rows
# Python Pandas printing last 5 rows


# import pandas as pd
#
# df=pd.read_csv("Automobile_data.csv")
# print("The CSV Data::",df)
# print(df.head(5))  # first five data
# print(df.tail(5)) # last five data








# Exercise 2: Clean the dataset and update the CSV file
# Replace all column values which contain ?, n.a, or NaN.


# import pandas as pd
#
# df=pd.read_csv("Automobile_data.csv")
#
# na_values={
# 'price':["?","n.a"],
# 'stroke':["?","n.a"],
# 'horsepower':["?","n.a"],
# 'peak-rpm':["?","n.a"],
# 'average-mileage':["?","n.a"]}
#
# print (df)
#
# df.to_csv("Automobile_data.csv")



# Exercise 3: Find the most expensive car company name
# Print most expensive car’s company name and price.


# index   company        price
# 35    mercedes-Benz  45400.0


# import pandas as pd
#
# df=pd.read_csv("Automobile_data.csv")
# print(df [['company','price']][df.price==df['price'].max()])
# print(df['price'].max())
# print(df.groupby(['company'])['price'].max())          #groupby method






# Exercise 4: Print All Toyota Cars details

# import  pandas as pd
#
# df=pd.read_csv("Automobile_data.csv")
# grouped = df.groupby('price').sum()
# z=grouped.to_csv('Automobile_data.csv',index=True)
# print(grouped)


# import pandas as pd
# df=pd.read_csv("Automobile_data.csv")
# car_Manufacturers = df.groupby('company')
# toyotaDf = car_Manufacturers.get_group('toyota')
# print(car_Manufacturers)
# print(toyotaDf)


#
# Exercise 5: Count total cars per company
#
# import pandas as pd
#
# df=pd.read_csv("Automobile_data.csv")
#
# print(df['company'].value_counts())
#




# Exercise 6: Find each company’s Higesht price car

# import pandas as pd
#
# df=pd.read_csv("Automobile_data.csv")
# print(df.groupby(['company'])['price'].max())





# # Exercise 7: Find the average mileage of each car making company
# average means  mean


# import pandas as pd
#
# df=pd.read_csv("Automobile_data.csv")
# print(df.groupby(['company'])['average-mileage'].mean())





# Exercise 8: Sort all cars by Price columns

# import pandas as pd
#
# df=pd.read_csv("Automobile_data.csv")
# print(df.sort_values(['price']))





# Exercise 9: Concatenate two data frames using the following conditions
# GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
# japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

# import pandas as pd
#
# df=pd.read_csv("Automobile_data.csv")
# GermanCars = {
#     'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
#     'Price': [23845, 171995, 135925 , 71400]
# }
#
# z=pd.DataFrame(GermanCars)
# print(z)
# japaneseCars = {
#     'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '],
#     'Price': [29995, 23600, 61500 , 58900]
# }
#
# k=pd.DataFrame(japaneseCars)
# print(k)



# Exercise 10: Merge two data frames using the following condition

# Create two data frames using the following two Dicts, Merge two data frames, and
# append the second data frame as a new column to the first data frame.


# Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
# car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}


# import pandas as pd
#
# df=pd.read_csv("Automobile_data.csv")
# print(df)
#
# Car_Price = {
#     'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
#     'Price': [23845, 17995, 135925 , 71400]
# }
# z=pd.DataFrame(Car_Price)
# print(z)
#
# car_Horsepower = {
#     'Company': ['Toyota', 'Honda', 'BMV', 'Audi']
#     , 'horsepower': [141, 80, 182 , 160]
# }
#
# k=pd.DataFrame(car_Horsepower)
# print(k)
# x=pd.merge(z,k)
# print(x)