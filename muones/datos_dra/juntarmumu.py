# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 17:01:01 2021

@author: Alan
"""
import pandas as pd
import csv
import numpy as np      
import matplotlib.pyplot as plt

df = pd.read_table('eventos_pxpypzE.csv',delimiter=',',header=None)

df_1=df.iloc[lambda x: x.index % 2 == 0]

df_1=df_1.reset_index(drop=True)

df_2=df.iloc[lambda x: x.index % 2 != 0]
df_2=df_2.reset_index(drop=True)
df_2.rename(columns= {#df_2.columns[0]:'masa*',
                      df_2.columns[0]: 'px*',
                      df_2.columns[1]: 'py*',
                      df_2.columns[2]: 'pz*',
                      df_2.columns[3]: 'E*'}, inplace=True)

df_3=df_1.join(df_2)
df_3.rename(columns= {df_3.columns[0]: 'E',
                      df_3.columns[1]: 'px',
                      df_3.columns[2]: 'py',
                      df_3.columns[3]: 'pz',})
print(df_3.head())
df_3.to_csv('mu+mu-.csv')
