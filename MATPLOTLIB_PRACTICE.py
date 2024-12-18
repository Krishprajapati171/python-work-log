# Question-1

#  Write a Python programming to display a bar chart of the popularity of programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7


# import  matplotlib.pyplot as pt
# import   numpy as np
#
# x=np.array(['java','Python','php','javascript','C#','C++'])
# y=np.array([22.2,17.6,8.8,8,7.7,6.7])
#
# chart=pt.bar(x,y)
# pt.xlabel('Languages')
# pt.ylabel('Popularity')
# pt.title('Popularity of the programming laguages')
# print(pt.show())
# print(chart)



# # Question-2
# Write a Python program to draw a scatter plot for three different groups camparing weights and heights.

# import matplotlib.pyplot as pt
# import numpy as np
#
# print('Group1')
# weight1=[67,57.2,59.6,59.64,55.8,61.2,60.45,61,56.23,56]
# height1=[101.7,197.6,98.3,125.1,113.7,157.7,136,148.9,125.3,114.9]
#
# print("Group2")
# weight2=[61.9,64,62.1,64.2,62.3,65.4,62.4,61.4,62.5,63.6]
# height2=[152.8,155.3,135.1,125.2,151.3,135,182.2,195.9,165.1,125.1]
#
# print('Group3')
# weight3=[68.2,67.2,68.4,68.7,71,71.3,70.8,70,71.1,71.7]
# height3=[165.8,170.9,192.8,135.4,161.4,136.1,167.1,235.1,181.1,177.3]
#
# Weight=np.concatenate((weight1,weight2,weight3))
# Height=np.concatenate((height1,height2,height3))
# print("Weight after concating::",Weight)
# print("Height after concating::",Height)
# pt.title("Group Wise weight VS Height Wise")
# pt.xlabel("Weight")
# pt.ylabel("Height")
# pt.scatter(Weight,Height,marker='*')
# pt.show()




# Question-3

# . Write a Python programming to create a pie chart with a title of the popularity of programming Languages.
# Make multiple wedges of the pie.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7



# import matplotlib.pyplot as pt
# import numpy as np
#
# x=np.array(['java','python','php','javascript','C#','C++'])
# y=np.array([22.2,17.6,8.8,8,7.7,6.7])
# pt.pie(y,labels=x)
# pt.xlabel('data')
# pt.ylabel('Languages')
# pt.show()



# Question-4
# Write a Python programming to create a Histogram chart with given ::

# import matplotlib.pyplot as pt
# import random
# import numpy as np
#
# x=np.random.randn(1000)
#
# pt.xlabel("Weight")
# pt.ylabel("Height")
# pt.hist(x,bins=30)
# pt.show()


