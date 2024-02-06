# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:36:43 2023

@author: ASUS
"""

import pandas as pd
import numpy as np

data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)
print(df)


'''
creating the function for adding 4

'''


def add_4(x):
    return x+4


'''

using .apply() to apply this method to the dataframe for addding function
add_4

'''

df = df.apply(add_4)
print(df)


'''
adding function to the specific columns 

'''


def add_3(x):
    return x+3


df[['A', 'B']] = df[['A', 'B']].apply(add_3)
print(df)


'''
creating lambda function for adding 4 

'''


def x(x): return x+4


y = df.apply(x)
print(y)


'''
insteaad of apply() using transform()

'''


def add_3(x):
    return x+3


df.transform(add_3)
print(df)


tech = {
    'Courses': ['Spark', 'PySpark', 'Hadoop', 'Python', 'Pandas', 'Hadoop', 'Spark', 'Pton', 'NA'],
    'Fee': [22000, 25000, 23000, 24000, 21000, 12000, 23000, 1230, 34000],
    'Duration': ['30days', '40days', '50days', '10days', '70days', '40days', '70days', '20days', '40days'],
    'Discount': [1000, 2300, 1000, 1200, 2500, np.nan, 1400, 1600, 0]

}
df = pd.DataFrame(tech)
df


x = df.groupby(['Courses']).sum()
print(x)


df2 = df.groupby(['Courses', 'Fee']).sum().reset_index()
print(df2)


x = df.columns
print(x)


column_head = list(df.columns)
print(column_head)


'''
shuffiling the given dataset 

'''

x = df.sample(frac=1)
print(x)

'''
will add the new index starting from the 0 rr

'''
y = df.sample(frac=1).reset_index()
print(y)


'''
this will remove the shuffled indexes and will only keep the new index
'''
z = df.sample(frac=1).reset_index(drop=True)
print(z)



'''
joining the two dataframes 


'''
import pandas as pd
import numpy as np
tech={
      'Courses':['Spark','PySpark','Python','Pandas'],
      'Fee':[22000,25000,23000,24000],
      'Duration':['30days','35days','35days','50days'],
      
      }
labels=['r1','r2','r3','r4']

df1 = pd.DataFrame(tech, index = labels)
print(df1)


tech1 = {'Courses':['Data Science','Spark','Python','Go'],
         'Discount':[344,756,265,4567]}

labels1 = ['r1','r6','r3','r5']

df2 = pd.DataFrame(tech1, index = labels1)
print(df2)

'''
left join 

'''

x = df1.join(df2, lsuffix='_left', rsuffix='_right')
print(x)



'''
inner join due to explaining how = 'inner'

'''

df3 = df1.join(df2, lsuffix='_l', rsuffix='_r', how="inner")
print(df3)



df3 = df1.join(df2, lsuffix='_left', rsuffix='_rigth', how='right')
print(df3)



df4 = df1.set_index('Courses').join(df2.set_index('Courses'),how='inner')
print(df4)



df5 = df1.set_index('Courses').join(df2.set_index('Courses'), how = 'left')
print(df5)



import pandas as pd
import numpy as np
tech={
      'Courses':['Spark','PySpark','Python','Pandas'],
      'Fee':[22000,25000,23000,24000],
      'Duration':['30days','35days','35days','50days'],
      
      }
labels=['r1','r2','r3','r4']

df1 = pd.DataFrame(tech, index = labels)
print(df1)


tech1 = {'Courses':['Data Science','Spark','Python','Go'],
         'Discount':[344,756,265,4567]}

labels1 = ['r1','r6','r3','r5']

df2 = pd.DataFrame(tech1, index = labels1)
print(df2)



df3 = pd.merge(df1, df2)
print(df3)





#################################################################



import pandas as pd

df1 = pd.DataFrame({ 'courses': ['Spark','PySpark','Python','Pandas'],
                    'Fees':[20000, 40000, 7654, 3000]})

df2 = pd.DataFrame({'courses':['Pandas','Hadoop','Hyperion','Java'],
                    'Fees':[2855,7399,7493,9004]})

df3 = pd.DataFrame({'Duration':['30 days','35 days','29 days','7 days'],
                    'Discount':[1000,3467,1233,2333]})
print(df1)
print(df2)
print(df3)

data = df1, df2

'''
concatinating the df1 and df2

'''

df7 = pd.concat(data)
print(df3)

'''
concatinating and adding the new index strting from 0 

'''
df8 = pd.concat(data).reset_index()
print(df4)


'''
concatinating and after adding new indexes we can remove the other indexes 
by drop = True

'''
df9 = pd.concat(data).reset_index(drop = True)
print(df5)


'''
concatinating the multiple dataframes 

'''

info = df1, df2, df3

df0 = pd.concat(info)
print(df0)














