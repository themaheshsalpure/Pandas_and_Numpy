# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 23:13:48 2023

@author: ASUS
"""



import pandas as pd

x = pd.read_csv('bmw.csv')
print(x.head)

df = pd.DataFrame(x)
n = df.isnull()
print(n)



'''

we are acessing the requiredd columns only from the dataset by using their indexes
'''
y = df.iloc[:,16:18]
print(y)




'''
this will get the all related information about the dataset 
'''
print(y.info())
print(y.describe())




'''
accessing any specific column from the dataset by using usecol method

'''
import pandas as pd 
dr = pd.read_csv('bmw.csv', usecols=['price'])
print(dr)
df = pd.DataFrame(dr)
print(df)



'''
here we can access the price values where the price is greater than the 50000

'''

x = df[df['price']>50000]
print(x)

























