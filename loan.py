
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:01:00 2023

@author: ASUS
"""

# 📌🐍 -----------------------------------------------------------------------


import pandas as pd

x = pd.read_csv('C:\\2-Dataset\\loan.csv')
print(x)
print("\n")


'''
 creating the data frame of the dataaset 
'''
df = pd.DataFrame(x)
print(df)

'''
slicing the dataset

'''
frag = df.iloc[0:11,:]
print(frag)


print('\n')


'''
 describing the dataset

'''
y = frag.describe()
print(y)

print('\n')


'''
checking the shape of the dataset

'''
shape = df.shape
print(f"shape of the dataset is : {shape}")

print('\n')


'''
 checking the size of the dataset

'''
row = df.size
print(f'size of the dataset : {row}')



'''
 getting the names of the columns in the dataset 

'''
columns = df.columns
print(columns)
print('\n')
for i in columns:
    print(i)


'''

 fetching the murder column only from the dataset
'''

murder = df['member_id']
print(murder)



'''
Renaming the columns 

'''
import pandas as pd

x = pd.read_csv('C:\\2-Dataset\\loan.csv')
print(x)
print("\n")
df = pd.DataFrame(x)
print(df)
print('\n')

x = df.rename({'member_id':'m_id'}, axis='columns')
print(x)
print('\n')



'''
first taking only two columns from the dataset
creating the dataframe of the only two columns fromt the dataset

'''

import pandas as pd

x = pd.read_csv('C:\\2-Dataset\\loan.csv', usecols=['member_id','id'])
print(x)
print("\n")
df = pd.DataFrame(x)
print(df)
print('\n')



'''
------------------ using iloc()
'''


# accessing elements from 1 to 20
x = df.iloc[0:21,:]
print(x)


'''
reversing the given data 
'''
x = df.iloc[::-1]
print(x)


x = df.iloc[:,:-1]
print(x)


x = df.iloc[:,-1]
print(x)



'''
Accessing column from the df using loc() 
'''
x = df.loc[:,['id']]
print(x)


[]



import pandas as pd

x = pd.read_csv('C:\\2-Dataset\\loan.csv')
print(x)
print("\n")
df = pd.DataFrame(x)
print(df)

d1 = df.drop[:['id']]
print(d1)


























