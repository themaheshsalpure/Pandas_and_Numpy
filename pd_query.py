# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:15:43 2023

@author: ASUS
"""

import pandas as pd

data={
      'courses':['sparks','PySpark','Hadoop','Python','Matplot'],
      'Fee':[2000,1000,3000,3400,2300],
      'Duration':['20days','30days','50days','40days','45days'],
      'Discount':[10,20,30,40,50]}

df = pd.DataFrame(data)
print(df)


# for gettingg the specific course data from the dataframe

df2 = df.query("courses == 'sparks'")
print(df2)


df3 = df.query("courses != 'sparks'")
print(df3)



"""
assigning the new column in dataframe 
adding the new columns

"""

tutor = ['ram','charan','raja','mouli','chrostopher']

df2 = df.assign(Tutors = tutor)
print(df2)

'''
Adding multiple columns 

'''
tutor = ['ram','charan','raja','mouli','chrostopher']
mnc = [1,2,3,4,5]



df4 = df.assign(MNC = mnc , Tutor = tutor )
print(df4)



'''
using lambda function to create a new discount column 
'''

df5 = df.assign(discount = lambda x: x.Fee * x.Discount / 100)
print(df5)



'''
Another way of adding the new column

'''
mnc = [1,2,3,4,5]
df['MNC Companies'] = mnc
print(df)



'''
adding the new column at the specific position

'''

df = pd.DataFrame(data)
tutor = ['ram','charan','raja','mouli','chrostopher']


# df.insert(locaton, desired_col_name, col_data)

df.insert(0, 'Tutors',tutor)
print(df)


'''
counting the number of rows and number of columns 

'''
# rows 
rows = len(df.index)
print(rows)

rows = len(df.axes[0])
print(rows)

rows = df.shape[0]
print(rows)


# columns 
columns = len(df.columns)
print(columns)

columns = len(df.axes[1])
print(columns)

columns = df.shape[1]
print(columns)












