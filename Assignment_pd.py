# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:01:08 2023

@author: ASUS
"""


# 📌🐍 -----------------------------------------------------------------------

'''
write pandas program to create df from dictionary adn display it 

'''


import pandas as pd

data = {'x':[2,5,7,2,5],
        'y':[9,12,54,78,34],
        'z':[67,87,34,76,45]}

df = pd.DataFrame(data)
print(df)

# 📌🐍 -----------------------------------------------------------------------

'''
write pandas program to create dataframe with the specified labels 

'''

import pandas as pd
import numpy as np

data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan ,9,20,14.5,np.nan ,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }


labels = ['a','b','c','d','e','f','g','h','i','j']

x = pd.DataFrame(data, index=labels)
print(x)


# 📌🐍 -----------------------------------------------------------------------

'''
data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

'''



# 📌🐍 -----------------------------------------------------------------------




'''
write pandas program to display summery pf basic information abount the df and its data

'''

import pandas as pd

data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

df = pd.DataFrame(data)
print(df)

print(df.describe())
print(df.info())



# 📌🐍 -----------------------------------------------------------------------


'''
write pandas to get first three rows of the given dataframe
'''

import pandas as pd

data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = [1,2,3,4,5,6,7,8,9,10]
df = pd.DataFrame(data, index = labels)
print(df)

print('First 3 rows of the dataframe : \n')

x = df.iloc[:3,:]
print(x)


# 📌🐍 -----------------------------------------------------------------------

'''
write pandas program to select name and score column from the dataframe 

'''

import pandas as pd


data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = [1,2,3,4,5,6,7,8,9,10]


df = pd.DataFrame(data, index = labels)

x = df.loc[:,['name','score']]
print(x)


# 📌🐍 -----------------------------------------------------------------------

'''
write pandas program to select the specific columns and rows 


'''

data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = [1,2,3,4,5,6,7,8,9,10]

df = pd.DataFrame(data, index = labels)
print(df)

# using iloc
x = df.iloc[1:7,1:3]
print(x)


# using loc
y = df.loc[1:7,'score':'attempts']
print(y)



# 📌🐍 -----------------------------------------------------------------------

'''
write program to select rows where the number of attempts in the examimation is
greater than 2  

'''
import pandas as pd
import numpy as np

data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = [1,2,3,4,5,6,7,8,9,10]


df = pd.DataFrame(data , index = labels)
print(df)

# type 1 
x = df.loc[df.attempts>2]
print(x)

# type 2 
x = df[df['attempts']>2]
print(x)

# 📌🐍 -----------------------------------------------------------------------

'''
write a program to count the number of row and columns in the dataframe 

'''

import pandas as pd
import numpy as np

data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = [1,2,3,4,5,6,7,8,9,10]


df = pd.DataFrame(data, index = labels )
print(df)




row_len = len(df.index)
print(row_len)

columns_len = len(df.columns)
print(columns_len)


row = len(df.axes[0])
print(row)

column = len(df.axes[1])
print(column)


row = df.shape[0]
print(row)

column = df.shape[1]
print(column)

# 📌🐍 -----------------------------------------------------------------------

'''0
write pandas program to select the rows where the score is missing 


'''

import pandas as pd
import numpy as np


data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = [1,2,3,4,5,6,7,8,9,10]


df = pd.DataFrame(data, index=labels)

print(df)

df2 = (df[df['score'].isnull()])
print(df2)                    


# 📌🐍 -----------------------------------------------------------------------

'''
write a program to select the rows having score between 15 and 20

'''           
import pandas as pd
import numpy as np

data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = [1,2,3,4,5,6,7,8,9,10]

df = pd.DataFrame(data, index = labels)

print(df)


df2 = (df[df['score'].between(15,20)])
print(df2)




df2 = df[df['score'].isnull()]
print(df2)

# 📌🐍 -----------------------------------------------------------------------

'''
write program to select the rows where the number of attemtp in exam is less than two and score 
is greater than 15

'''

import pandas as pd
import numpy as np

data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = [1,2,3,4,5,6,7,8,9,10]

df = pd.DataFrame(data, index = labels)
print(df)


x = (df[(df['score']>15) & (df['attempts']<2)])
print(x)


# 📌🐍 -----------------------------------------------------------------------


'''
write python program to change the score of row d with 11.5

'''

data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(data, index = labels)
print(df)

df.loc['d','score'] = 11.5
print(df)


# 📌🐍 -----------------------------------------------------------------------

'''
write python program to create the sum of examination attempts 

'''

data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = [1,2,3,4,5,6,7,8,9,10]

df = pd.DataFrame(data, index = labels)


# first way 
x = df['attempts'].sum()
print(x)


# second way 
x = df['attempts']
print(x)
c = 0
for i in x :
    c+=i

print(c)


# 📌🐍 -----------------------------------------------------------------------


'''
write pandas program to calculate mean of all students score 

'''


data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = [1,2,3,4,5,6,7,8,9,10]


df = pd.DataFrame(data, index = labels )
print(df)

mean = df['score'].mean()
print(mean)




# 📌🐍 -----------------------------------------------------------------------


'''
write program to append the new row k to data frame with given values for each row 

'''

x = ['suresh','20.5','2','yes']

data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = ['a','b','c','d','e','f','g','h','i','j']


df = pd.DataFrame(data, index = labels )
# print(df)

df.loc['k']=x
print(df)


# 📌🐍 -----------------------------------------------------------------------

'''
write pandas program to sort dataframe 

1 ] by name is descending order
2 ] by score in descending order 

'''

import pandas as pd
import numpy as np

data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(data, index = labels)
print(df)


# first = df[df['name']].sort()
# print(first)


df1 = df.sort_values(by=['name','score'], ascending=[False, True])
print(df1)


# sorting by name 
first = df.sort_values(by=['name'], ascending = [False])
print(first)

# sorting by score
second = df.sort_values(by=['score'], ascending=[True])
print(second)

# 📌🐍 -----------------------------------------------------------------------

'''
write program to replace qqualify column content values yes and no with 
true and false

'''


data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(data, index = labels)

# mapping of the old values with the new values 
df['qualify'] = df['qualify'].map({'yes':True, 'no':False})
print(df)


# 📌🐍 -----------------------------------------------------------------------


'''
write python program to change varad name with harsh in name column

'''




data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(data, index = labels)

df['name'] = df['name'].replace('navnath','harsh')
print(df)


# 📌🐍 -----------------------------------------------------------------------

'''
write program to insert new column to the existing daataframe

'''



data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = ['a','b','c','d','e','f','g','h','i','j']

color = ['red','green','blue','yello','white','black','purple','gray','brown','pink'] 

df = pd.DataFrame(data, index = labels)

df.insert(4, 'colours', color)
print(df)





import pandas as pd
import numpy as np
data = {
        'name':['ram','mahesh','harsh','yuvraj','rahul','aditya','navnath','akshay','sanket','varad'],
        'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        'attempts':[1,3,2,3,2,3,1,1,2,1],
        'qualify':['yes','no','yes','no','no','yes','yes','no','yes','no']
        }

labels = ['a','b','c','d','e','f','g','h','i','j']

color = ['red','green','blue','yello','white','black','purple','gray','brown','pink'] 

df = pd.DataFrame(data, index = labels)
print(df)

df.assign(colur = color)
print(df)





import pandas as pd

d = {
     'c1':[1,2,3,4,5],
     'c2':[6,7,8,9,10],
     'c3':[3,2,8,7,5],
     'c4':[2,6,9,4,0]
     }

df = pd.DataFrame(d)
print(df)


x = df.loc[:,'c1']
print(x)
print(type(x))


c = pd.Series(x)
print(c)



import pandas as pd
data = [['red','green','blue'],
        ['red','violet'],
        ['red','blue','black']
        ]

x = pd.Series(data)
print(x)

d = x.apply(pd.Series).stack().reset_index(drop = True)
print(d)

c = x.apply(df.Series).stack().reset_index(drop = True)
print(df)

s1 = [1,2,3,4]
s2=[5,6,7,8,9]
x = pd.Series(s1)
y = pd.Series(s2)

s4 = pd.concat([x,y] ).reset_index(drop = True)
print(s4)
























































































