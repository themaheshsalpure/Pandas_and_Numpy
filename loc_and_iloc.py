# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 10:18:31 2023

@author: ASUS
"""

import pandas as pd
# data = pd.read_csv('nba.csv')
# df = pd.DataFrame(data)
# print(df)


data = {'courses':['cyber Security', 'Data Science', 'AI and ML','Web Development'],
        'prices':[2000,3000,4000,6000],
        'Duration':['2 months','3 months','1 month','4 months'],
        'Discount':[20,45,34,65]
        }
row = ['r1','r2','r3','r4']

df = pd.DataFrame(data, index=row)
print(df)


'''
accessing the perticular data part from the dataset using .iloc
method 
'''
dw = df.iloc[1:,1:]
print(dw)

da = df.iloc[1:3,1:3]
print(da)


# selecting only 2 and 3 number of rows
ds = df.iloc[[2,3]]
print(ds)

# this will select the last roww in the data
dg = df.iloc[-1:]
print(dg)

# this will select the first row from the datafrme
dh = df.iloc[:1]
print(dh)


# will select the last three rows 
gh = df.iloc[-3:]
print(gh)


dg = df.iloc[::2]
print(dg)



'''
Accessing rows using the direct names of the rows 

'''

dg = df.loc['r1']
print(dg)

dg = df.loc['r2':'r4']
print(dg)

# accessing rows using row names with setp of 2 
dg = df.loc['r1':'r4':2]
print(dg)


# accessing multiple rows at once
dg = df.loc[['r1','r2','r4']]
print(dg)


# accessing the columns using the loc()
dg = df.loc[:,['courses','prices']]
print(dg)


dg = df.loc[{'courses':'sub'}]
print(dg)



































