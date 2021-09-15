# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 01:21:10 2021

@author: Alan
"""

import pandas as pd
import csv
import numpy as np      
import matplotlib.pyplot as plt

df=pd.read_table("muones.csv",delimiter=',',header=None)

df.rename(columns = {df.columns[0]:'datos'},inplace=True)

df=df['datos'].str.split('  ',n=12,expand=True)
print(df.head())

f=df[12].str.split(' ',n=7,expand=True)
f=f.drop(df.columns[0],axis=1)
print(f)
g1= df.filter([3]).copy()
g1.rename(columns={g1.columns[0]: 0},inplace=True)
g2=f.filter([1,2,3,4,5,6,7]).copy()
g=g1.join(g2)
print(g.head())

g = g.astype(float)
g.rename(columns= {g.columns[0]:'masa',
                   g.columns[1]: 'px',
                   g.columns[2]: 'py',
                   g.columns[3]: 'pz',
                   g.columns[4]: 'E',
    },inplace=True)

for i in range(5,7):
    g=g.drop(g.columns[i],axis=1)
g=g.drop(g.columns[5],axis=1)
g.to_csv('momento.csv')


print(g.head())

plt.figure(0)
plt.title('$P_x$')
plt.plot(g['px'])


plt.figure(1)
plt.hist(g['px'])

plt.figure(2)
plt.xlabel('P_x')
plt.ylabel('P_y')
plt.plot(g['px'],g['py'])

plt.figure(3)
plt.title('Momento transverso')

plt.hist(np.sqrt(g['px']**2+g['py']**2))
plt.savefig("momentotransverso.png", type='png')

plt.figure(4)
plt.title('Momento total')

plt.hist(np.sqrt(g['px']**2+g['py']**2+g['pz']**2) )
#plt.savefig("momentotransverso.png", type='png')


#plt.figure(0)
#g.hist(column=['momento en z'])
#plt.show()
#plt.plot.hist(column2)





#g[0,1]=g[11].str.split(' ',n=7)
#print(g)

#df[12].str.split(' ',n=8,expand=True)
#df.to_csv('pandas.csv')
#df=df.drop(df.columns[1],axis=1)
#df=df.drop(df.columns[0],axis=1)
#df.rename(columns = {df.columns[1]:'muones'},inplace=True)

#df.columns = df.columns.str.replace(' ', '')
#nan_value = float("NaN")
#df.replace(" ", nan_value, inplace=True)
#for i in range(0,3):
#    df[i] = np.nan
#    df.dropna(how='all', axis=1, inplace=True)
#df.drop(df.columns[2])
#df.rename(,inplace=True)


#df.str.split(' ')
#df=df.to_string(index=False)
#print(df.head())
#print(df.str.split(' '))
#df=df.reshape(14,)
