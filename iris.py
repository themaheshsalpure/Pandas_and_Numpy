# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:55:24 2023

@author: ASUS
"""

import sklearn 
from sklearn import datasets
import csv
import pandas as pd



x = sklearn.datasets.load_iris()
x.to_csv('iris1.csv')

