#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
#array、arange、reshape用法
data=[1,2,3,4,5]
arr1=np.array(data)
arr2=np.arange(10)
arr3=np.arange(10).reshape(2,5)
arr4=np.random.randn(5,2)
arr5=np.random.randn(2,5)
#常用函数：sqrt开平方、mean平均数、std标准差、dot矩阵相乘、multiply数组相乘、around四舍五入
print 'sqrt---------------\n',np.sqrt(arr3)
print 'mean---------------\n',np.mean(arr3)
print 'std---------------\n',np.std(arr3)
print 'dot---------------\n',np.dot(arr3,arr4)
print 'multiply---------------\n',np.multiply(arr3,arr5)
print 'around---------------\n',np.around(arr5,2)

import pandas as pd
#pd读写文件：read_csv、to_csv、read_excel、to_excel
#pd常用数据结构： Series 和 DataFrame
s=pd.Series([1,2,3],index=['a','b','c'])
print  'Series---------------\n',s
data={'A':pd.date_range('20180226',periods=5),
      'B':[12,33,-22,34,51],
      'C':pd.Categorical(['pass','pass','fail','pass','hehe'])}
df=pd.DataFrame(data)
print 'df---------------\n',df
df2=pd.DataFrame(data,columns=['C','B','A'],index=list(range(1,6)))
print 'df2---------------\n',df2
#DataFrame，常用的方法：sort_values排序、dropna去除NA值、loc和iloc切片、append增加
# print 'df排序--------------\n',df.sort_values(by='B',ascending=False)
from numpy import nan as NA
data=pd.DataFrame([[1.,-2,3],[NA,3,3],[NA,NA,2]])
print 'df去除NA--------------\n',data.dropna()
print 'df,loc切片--------------\n',df.loc[:,'B']
print 'df,iloc切片--------------\n',df.iloc[0:3,0]