# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:05:43 2023

@author: ASUS
"""
# 📌🐍 -----------------------------------------------------------------------


'''
python program to create one serie comprises of 2,4,6,8,10

'''

import pandas as pd

data = [2,4,6,8,10]
x = pd.Series(data)
print(x)



# 📌🐍 -----------------------------------------------------------------------

'''
write a python program to convert a pandas module series to python list and its type

converrting the paanda series to the python list 
'''

import pandas as pd
data = [2,4,6,8,10]
x = pd.Series(data)
print(x)
print(x.dtype)


y = x.tolist()
print(y)
print(type(y))

'''
add python program to add, substract, multiply 
sample series - [2,4,6,8,10], [1,3,5,7,9]


'''

s1 = [2,4,6,8,10]
s2 = [1,3,5,7,9]

s3 = pd.Series(s1)
s4 = pd.Series(s2)

x = s3+s4
print(f'addition of the series : {x}')

y = s3-s4
print(f'Substraction of the series : {y}')

z = s3*s4
print(f'multiplication of the series : {z}')


a = s3/s4
print(f'division of the series : {a}')


# 📌🐍 -----------------------------------------------------------------------

'''
write python program to compare two series 

comparing the given pandas series 
'''

import pandas as pd

s1 = pd.Series([2,4,6,8,10])
s2 = pd.Series([1,3,5,7,9])


print(f'Equals : {s1==s2}')
print(f"Greater than : {s1>s2}")
print(f"Less than : {s1<s2}")



# 📌🐍 -----------------------------------------------------------------------


'''
converting the dictionary to the pandas series 

'''

import pandas as pd

d1 = {'a':100,'b':200,'c':300,'d':400}
s = pd.Series(d1)
print(f'Dictionary converted to the pandas series is as : {s}')



# 📌🐍 -----------------------------------------------------------------------

'''
program to convert numpy array into the pandas series

'''
import numpy as np
import pandas as pd

data = [2,4,6,8,10]
x = np.array(data)
print(f'the numpy array is as : {x}')
# print(type(x))
y = pd.Series(x)
print(f'the numpy array converted to the pandas string as : {y}')


# 📌🐍 -----------------------------------------------------------------------

'''
pandas program to change the data type of the column or given series 

'''

import pandas as pd
s1 = pd.Series(['100','200','300','400'])
print(s1.dtype)

x = pd.to_numeric(s1, errors = 'ignore')
print(x.dtype)


# 📌🐍 -----------------------------------------------------------------------

'''
write python program to convert the first column of the dataframe as series 

'''

import pandas as pd

d = {
     'c1':[1,2,3,4,5],
     'c2':[6,7,8,9,10],
     'c3':[3,2,8,7,5],
     'c4':[2,6,9,4,0]
     }

df = pd.DataFrame(d)
print(df)

# getting series output 
y = df.iloc[:,0]
print(type(y))

# getting the frame output
x= df.iloc[:,:1]
print(x)
print(type(x))

# 📌🐍 -----------------------------------------------------------------------


'''
stack() method in pandas

'''

import pandas as pd
data = [['red','green','blue'],
        ['red','violet'],
        ['red','blue','black']
        ]

x = pd.Series(data)
print(x)

'''
.stack() will stack the seperate data and concatenate all the data then reset_index(drop=True) will
reset the initial indexes and after concatination it will assign the new indexes to all the concatinated
data 

'''
a = x.apply(pd.Series).stack().reset_index(drop=True)
print(a)

# 📌🐍 -----------------------------------------------------------------------

'''
write pandas program to add some data to an existing series

'''

import pandas as pd

s = pd.Series([2,4,6,8])
q = pd.Series([10,12])
x = pd.concat([s,q], ignore_index=True)

print(x)




# 📌🐍 -----------------------------------------------------------------------

'''

write python program to sort a givven series 

'''
import pandas as pd

s = pd.Series([4,7,2,9,4,5,7])
x =s.sort_values()
print(x)

# 📌🐍 -----------------------------------------------------------------------

'''
write python program to change the order of index of a given series 

'''
# without using reindex() method 

import pandas as pd
s = pd.Series([1,2,3,4,5,6], index=['a','b','c','d','e','f'])
print(s)

index = ['f','e','d','c','b','a']
x = pd.Series(s,index=index)
print(x)


# using reindex() method
import pandas as pd
s = pd.Series([1,2,3,4,5,6], index=['a','b','c','d','e','f'])


x = s.reindex(index = ['f','e','d','c','b','a'])
print(x)

















































































