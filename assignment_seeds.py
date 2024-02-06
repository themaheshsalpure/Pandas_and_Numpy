# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:33:34 2023

@author: ASUS
"""

# 📌🐍 -----------------------------------------------------------------------


import pandas as pd


x = pd.read_csv('Seeds_data.csv')
print(x)


'''
creating the dataframe of the data 

'''
df = pd.DataFrame(x)
print(df)


# 📌🐍 -----------------------------------------------------------------------

'''
checking the information of the data 

'''
x = df.info()
print(x)

y = df.describe()
print(y)


# 📌🐍 -----------------------------------------------------------------------

'''
finding the mean of the area
sort

'''

mean = df['Area'].mean()
print(mean)


# 📌🐍 -----------------------------------------------------------------------

'''
adding the Area values to find the total area  

'''

add = df['Area'].sum()
print(add)



add = df['Perimeter'].sum()
print(add)


# 📌🐍 -----------------------------------------------------------------------

'''
sorting the area column with ascending order

'''

df1 = df.sort_values(by=['Area'], ascending=[False])
print(df1)
 


# 📌🐍 -----------------------------------------------------------------------



'''
getting the first row of the given column

'''


import pandas as pd


x = pd.read_csv('Seeds_data.csv')
print(x)
df = pd.DataFrame(x)
print(df)

df1 = df.iloc[:10,:]
print(df1)



df2 = df1.loc[:,['Area','Compactness']]
print(df2)


# 📌🐍 -----------------------------------------------------------------------
'''
renaming the column Area with area

'''



import pandas as pd


x = pd.read_csv('Seeds_data.csv')
print(x)
df = pd.DataFrame(x)
print(df)

df['Area'] = df.rename({'Area':'area'})
print(df)



x = df['Perimeter ']
print(x)
l = []

for i in x:
    l.append(i)
print(l)

df.insert(1, 'Perimeter',l )
print(df)



# 📌🐍 -----------------------------------------------------------------------


import pandas as pd

data = pd.read_csv('Seeds_data.csv')
print(data)

df = pd.DataFrame(data)
print(df)


# 📌🐍 -----------------------------------------------------------------------

'''
finding the total area by taking summation of area column

'''

addt = df['Area'].sum()
print(addt)


add1 = df['Perimeter '].sum()
print(add1)


# 📌🐍 -----------------------------------------------------------------------

'''
renaming the column name Perimeter 

'''
df.rename(columns={'Perimeter ':'Perimeter'}, inplace=True)
print(df)


# 📌🐍 -----------------------------------------------------------------------


'''
accessing the new Perimeter names column 

'''
x = df['Perimeter']
print(x)



print(df)


# 📌🐍 -----------------------------------------------------------------------



'''
selecting the perticular rows and columns from the dataset

'''

x = df.iloc[:16,:5]
print(x)


y = x.loc[:,['Area','Perimeter']]
print(y)



# 📌🐍 -----------------------------------------------------------------------


'''
sorting the Area columns 

'''

y = x.sort_values(by = 'Area', ascending = True)
print(y)



z = x.sort_values(by = "Perimeter", ascending = False)
print(z)


# 📌🐍 -----------------------------------------------------------------------


'''
Fetching all the information about the data file 

'''
a = x.describe()
print(a)

b = x.info()
print(b)


# 📌🐍 -----------------------------------------------------------------------


'''
properties

'''

df.shape[0]
df.shape[1]
df.size
df.columns
df.columns.values



# 📌🐍 -----------------------------------------------------------------------


'''
 iloc: by indexing

'''

df.iloc[:10,:3]
df.iloc[:,2:]
df.iloc[:10,:]
df.iloc[1:11,:4]


# 📌🐍 -----------------------------------------------------------------------


'''
 drop

'''
df2=df.drop(['Area','Perimeter '], axis=1) #axis=1 is for column
df2
rows=[0,1,2,3,4,5,6,7,8,9]
df3=df.drop(rows,axis=0) #axis=0 for rows
df3



# 📌🐍 -----------------------------------------------------------------------


'''
 condition

'''

df3=df[df['Area']>15]
df3

df4=df[(df['Area']>15) & (df['Perimeter ']>15)]
df4

# 📌🐍 -----------------------------------------------------------------------


'''
 .between(,)

'''

df3=df[df['Area'].between(17,20)]
df3


# 📌🐍 -----------------------------------------------------------------------

'''
 changing specific row value of any any column

'''

df.loc[1,'Area']=19
print(df.loc[:10,'Area'])


# 📌🐍 -----------------------------------------------------------------------

'''
working on small data

'''

df5=df.loc[:10,['Area','Perimeter ','length']]
df5


# 📌🐍 -----------------------------------------------------------------------

'''
add new column to df5

'''
    
df5=df.loc[:10,['Area','Perimeter ','length']]
l1=[0,2,4,6,8,10,12,14,16,18,20]
df6=df5.assign(Keys=l1)
df6

# 📌🐍 -----------------------------------------------------------------------




















