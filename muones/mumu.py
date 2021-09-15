# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:17:22 2021

@author: Alan
"""

import pandas as pd
import csv
import numpy as np      
import matplotlib.pyplot as plt

df = pd.read_table('momento.csv',delimiter=',')
df_1=df.iloc[lambda x: x.index % 2 == 0]
df_1=df_1.drop(df_1.columns[0],axis=1)
df_1=df_1.reset_index(drop=True)
df_2=df.iloc[lambda x: x.index % 2 != 0]
df_2=df_2.drop(df_2.columns[0],axis=1)
df_2=df_2.reset_index(drop=True)

df_2.rename(columns= {df_2.columns[0]:'masa*',

                      
                      df_2.columns[1]: 'px*',
                      df_2.columns[2]: 'py*',
                      df_2.columns[3]: 'pz*',
                      df_2.columns[4]: 'E*',
    },inplace=True)
df_3=df_1.join(df_2)

print(df_3.head())

df_3.to_csv('mu+mu-.csv')

#print(df.iloc[2])
#for i in range(10000):
    
#    f=df.iloc[2*i+1].copy()


#print(f.head())
