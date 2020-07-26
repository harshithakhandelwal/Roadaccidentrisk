# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:27:43 2019

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('new 4g.csv')
"""
b=df['Causes']

a=b.str.count('1').value_counts()
c=b.str.count('2').value_counts()
d=b.str.count('3').value_counts()
e=b.str.count('4').value_counts()
f=b.str.count('5').value_counts()
g=b.str.count('6').value_counts()
h=b.str.count('7').value_counts()
i=b.str.count('8').value_counts()
j=b.str.count('9').value_counts()


list1=[a,c,d,e,f,h,j]

#list=list(list[0][0],list[1][0],list[2][0],list[3][0],list[4][0],list[5][0],list[6][0])

list1=list1[0][0],list[1][1],list[2][0],list[3][0],list[4][0],list[5][0],list[6][0]
pd.Series(list1)
list2=pd.Series(['1','2','3','4','5','7','9'])
sns.barplot(x=list2,y=list1)

print(list1,list2)
"""

b=df['Classification of Accident']

a=b.str.count('1').value_counts()
c=b.str.count('2').value_counts()
d=b.str.count('3').value_counts()
e=b.str.count('4').value_counts()
#f=b.str.count('5').value_counts()
#g=b.str.count('6').value_counts()
#h=b.str.count('7').value_counts()
#i=b.str.count('8').value_counts()
#j=b.str.count('9').value_counts()


list1=[a,c,d,e]

#list=list(list[0][0],list[1][0],list[2][0],list[3][0],list[4][0],list[5][0],list[6][0])

list1=list1[0][0],list[1][1],list[2][0],list[3][0]
pd.Series(list1)
list2=pd.Series(['1','2','3','4'])
sns.barplot(x=list2,y=list1)

print(list1,list2)


