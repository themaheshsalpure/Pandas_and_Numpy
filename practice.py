# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 22:09:59 2023

@author: ASUS
"""

# 📌🐍 -----------------------------------------------------------------------

'''
getting indexes of the series 

'''

import pandas as pd

l2 = [1,2,3,4]
l1 = pd.Series(l2)
indexes = l1.index
print(indexes)
for i in indexes:
    print(i)
    
    
l = {'name':'mahesh','age':21, 'city':'astagaon','last name':'salpure'}
x = pd.Series(l)
y = x.index
print(y)
for i in y:
    print(i)
    
    
    
data = [10,20,30,40]
index = ['first','second','third','fourth'] 
x = pd.Series(data, index)   
print(x)
print(type(index))
    
    
    
data = [1,2,3,4]
index = ['first','first','second','fourth']    
x = pd.Series(data, index)
print(x)
    
    
data = [1,2,3,4,5,6]
del data[0]
print(data)



data = [10,20,30,40,None]
index = ['first','second','third','fourth','fifth'] 
x = pd.Series(data,index)
print(x.dtype)
print(x)



data = [10,20,30,40,None]
index = ['first','second','third','fourth','fifth']
x = pd.Series(data, index)
y = x.fillna(-1)
print(y)










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






'''
appending one series over the other series 

'''


data = [10,20,30,40,None]
index = ['first','second','third','fourth','fifth']

x = pd.Series(data, index)
print(x)



data = ['ms','aj','rj','ns']
index = [1,2,3,4]

a = pd.Series(data, index)
print(a)

 # appending the values of the x series to the series a 
y = a.append(x)
print(y)



# 📌🐍 -----------------------------------------------------------------------


import matplotlib.pyplot as plt

# x = pd.Series(np.random.randint(500))
# x.plot()
x = [1,2,3,4,5]
y = [5,6,7,8,9]
plt.plot(x, color = 'r')

plt.scatter(x, y)

























    
    
    
    
    
    
    
    
    
    