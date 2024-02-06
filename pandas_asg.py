# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 09:22:52 2023

@author: ASUS
"""

import pandas as pd

data = pd.read_csv('nba.csv')
# print(data)

df = pd.DataFrame(data)
print(df)



# dropping from the columns or dropping columns
dn = df.drop(['College'], axis=1)
print(dn)


'''
deleting the row number 0 from the dataset 
'''
ds = dn.drop(0)
print(ds)



# dropping the rows from the dataset

da = ds.drop(range(1,5))
print(da)





dw = da.drop(labels = ['Team'],axis=1)
print(dw)



'''
will drop the single column from the dataset using label 
'''
dw = da.drop(columns=['Age'], axis = 1)
print(dw)



'''
 this will drop the columns from the dataset from the
 index 3 and onwards 
'''
dw = da.drop(da.columns[3:], axis=1)
print(dw)



# this wil drop the two columns from the dataset 
df = da.drop(['Team','Number'], axis = 1)
print(df)


# deleting two columns at once
df = da.drop(da.columns[[5,7]], axis = 1)
print(df)


lis = ['Team','Number']
df = da.drop(lis, axis = 1)
print(df)













