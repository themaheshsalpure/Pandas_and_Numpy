# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:41:43 2023

@author: ASUS
"""

# 📌🐍 -----------------------------------------------------------------------

# Series - 

# here we are getting the index of the list items 

import pandas as pd

lst1 = pd.Series([10,20,30,40],name='count')

x = lst1.index
print(x)

    # Both are same 

import pandas as pd

lst1 = pd.Series([10,20,30,40])

x = lst1.index
print(x)


# 📌🐍 -----------------------------------------------------------------------

# providing index at our own insted of automatic indexing - 

'''
Here we are providing the index at our own 
when machine takes index automatically, it takes integer default indexes
but we are providing the index in the form of the strings 
Here it will show the indexes from the index list 

'''

songs1 = pd.Series([40,30,50,40],name = 'count', index = ['Mahesh','yuvraj','prafull','aditya'] )
 # here we created a series which is one dimensional list

 # here we provided the index for the series

x = songs1.index
print(x)
print(songs1)


# 📌🐍 -----------------------------------------------------------------------

'''
# Null values handling - 

'''
    
import pandas as pd 
    
# opening with absolute path

x = pd.read_csv('age.csv')
print(x)


import pandas as pd

x = pd.read_excel('Bahaman.xlsx')
print(x)


# 📌🐍 -----------------------------------------------------------------------


'''
using numpy 

'''

import numpy as np

arr1 = np.array([1,2,3,4,5,6])
print(arr1)
print(type(arr1))
arr1[0]                        # accessing the first element of the givrn array

y = arr1.mean()
print(f'the mean of arr1 is : {y}')


# 📌🐍 -----------------------------------------------------------------------


'''
quick reference question - 
    what is the difference between the list , series and array

'''

# 📌🐍 -----------------------------------------------------------------------


import pandas as pd


''' creating an series with indexes   
here we can create a list and can use the duplicate indexes 

'''
george = pd.Series([1,2,3], index=['1968','1970','1970'], name = 'main series')
# print(george)

# updating the values in the series 
george['1968'] = 0

# iterating through the series
for items in george:
    print(items)


# 📌🐍 -----------------------------------------------------------------------


'''
Deleting the values from the list

'''

lst1 = pd.Series(['m','y','a','n'], index = [1,2,3,4], name = 'xx')

del lst1[1]
print(lst1)



# 📌🐍 -----------------------------------------------------------------------


    
import pandas as pd

song1 = pd.Series([1,None,4,6], index = [1,2,3,4], name ='xx')
print(song1.dtype)

# converting one data type to the another data type 
# it wil give error bcz of the none value
pd.to_numeric(song1.apply(str),errors = 'coerce')    # error='coerce' ignores the error




# 📌🐍 -----------------------------------------------------------------------


'''

null value operations like - 
1 - we can replace the null value with any vaalue we want by using 
      y = x.fillna(value)
      
2 - we can remove the null value from the series by using 
     z = x.dropna()

'''
# replacing the null value with the desired value we want 

data = [10,20,30,40,None]
index = ['first','second','third','fourth','fifth']

x = pd.Series(data, index)
y = x.fillna(0)
print(y)


# removing the null value from the series 

data = [10,20,30,40,None]
index = ['first','second','third','fourth','fifth']

x = pd.Series(data, index)
y = x.dropna()
print(y)




# 📌🐍 -----------------------------------------------------------------------
'''

appending one series on another -

'''

import pandas as pd
song2 = pd.Series([10,16,21,30,42,50,42,30,21,16,10], index = [1,2,3,4,5,6,7,8,9,10,11], name = 'xx')

songs = song1.append(song2)
print(songs)




# 📌🐍 -----------------------------------------------------------------------

---------------- MATPLOTLIB -------------------------
'''
plotting series

'''

# 📌🐍 -----------------------------------------------------------------------


import matplotlib.pyplot as plt
fig = plt.figure()
song2.plot()
plt.legend()

# pp.plot(song2)





import matplotlib.pyplot as plt

fig = plt.figure()
song2.plot(kind='bar')
song1 .plot(kind='bar', color = 'r')
plt.legend()



import matplotlib.pyplot as plt

plt.title('Chomu graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
song2.plot(kind='bar')
song1.plot(kind='bar', color='r')
plt.legend()






'''
---------------------- histogram  --------------------------

'''






import matplotlib.pyplot as plt
import numpy as np

num = pd.Series(np.random.randn(500), name = 'xx')

fig = plt.figure()
ax = fig.add_subplot(111)
num.hist()




# 📌🐍 -----------------------------------------------------------------------

import pandas as pd
pd.__version__


# Creating an Data-Frame in pandas -

import pandas as pd
import numpy as np

tech = [['Chetan','20 days',30000],
      [ 'yuvraj','30 days',45000]]

y = np.array(df)
x = pd.DataFrame(y)
print(x)

print(type(df))





    import pandas as pd
import numpy as np


coloumn = ['name','year','value']
row = ['a','b']

df = pd.DataFrame(columns=coloumn, index = row)
print(df)




import pandas as pd
import numpy as np


data = {'courses':['cyber Security', 'Data Science', 'AI and ML','Web Development'],
        'prices':[2000,3000,4000,6000],
        'Duration':['2 months','3 months','1 month','4 months'],
        'Discount':[20,45,34,65]
        }

df = pd.DataFrame(data)
print(df)

print(type(df))



import pandas as pd
import numpy as np


df2 = df.convert_dtypes()
print(df2.dtypes)


# converted the data types 

import pandas as pd
import numpy as np

df2 = df.astype(str)
print(df2.dtypes)



import pandas as pd
import numpy as np
df2 = df.astype({'Discount': int, 'prices': int})
print(df2.dtypes)


# converting any specific coloumn data type -
cols = ['Discount','prices']
df[cols]=df[cols].astype(str)
df.dtypes


# thiis will ignore the errors - 

df2 = df.astype({'courses':int},errors='ignore')
df2.dtypes



# this will show the error - 
df2 = df.astype({'courses':int},errors = 'raise')
df2.dtypes


# 📌🐍 -----------------------------------------------------------------------


import pandas as pd

data = {'courses':['cyber Security', 'Data Science', 'AI and ML','Web Development'],
        'prices':[2000,3000,4000,6000],
        'Duration':['2 months','3 months','1 month','4 months'],
        'Discount':[20,45,34,65]
        }

df = pd.DataFrame(data)
df.to_csv('main.csv')

df.to_excel('ex.xlsx')




# 📌🐍 -----------------------------------------------------------------------

# exploratory data analysis 

import pandas as pd
import numpy as np

data = {'courses':['cyber Security', 'Data Science', 'AI and ML','Web Development'],
        'prices':[2000,3000,4000,6000],
        'Duration':['2 months','3 months','1 month','4 months'],
        'Discount':[20,45,34,65]
        }
row = ['r0','r1','r2','r3']

df = pd.DataFrame(data, index= row)
print(df)



x = df.shape
print(x)

y = df.size
print(y)


df.columns

df.columns.values

df.index


df.dtypes




# 📌🐍 -----------------------------------------------------------------------



import pandas as pd
import numpy as np

data = {'courses':['cyber Security', 'Data Science', 'AI and ML','Web Development'],
        'prices':[2000,3000,4000,6000],
        'Duration':['2 months','3 months','1 month','4 months'],
        'Discount':[20,45,34,65]
        }
row = ['r0','r1','r2','r3']

df = pd.DataFrame(data, index= row)
print(df)

# 📌🐍 -----------------------------------------------------------------------

'''
describe will give the all information about the dataframe like -
count
mean
std
min
25%
50%
75%
max

'''
x = df.describe()
print(x)



# 📌🐍 -----------------------------------------------------------------------

'''
Accessing the values of any specific column drom the dataframe

'''


df['prices']


# 📌🐍 -----------------------------------------------------------------------

'''
Accessing only the required number of the rows and columns 

'''
y = df.iloc[1:,1:3]
print(y)


# 📌🐍 -----------------------------------------------------------------------


df['prices']= df['prices']-3000

print(df)


# 📌🐍 -----------------------------------------------------------------------


'''
changing the names of the columns or renaming the columns of the dataframe

'''
df.columns =['a','b','c','d']
print(df)


# 📌🐍 -----------------------------------------------------------------------

'''
renaming the specific columns oof the dataframes with the custom name 

'''

x = df.rename({'a':'c1','b':'c2'}, axis='columns')
print(x)

########### or

x = df.rename({'c1':'a1','c2':'a2'}, axis=1)
print(x)



import pandas as pd
import numpy as np

data = {'courses':['cyber Security', 'Data Science', 'AI and ML','Web Development'],
        'prices':[2000,3000,4000,6000],
        'Duration':['2 months','3 months','1 month','4 months'],
        'Discount':[20,45,34,65]
        }
row = ['r0','r1','r2','r3']

df = pd.DataFrame(data, index= row)


y = df.rename(columns = {'courses':'a1','prices':'a2'})
print(y)













