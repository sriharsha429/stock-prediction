# -*- coding: utf-8 -*-
"""linear and ridge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zc3rLAr9-A6oTe-XxD9lhdOvOztff8Vu
"""



# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
# %matplotlib inline

from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

!pip install yfinance --upgrade --no-cache-dir
yf.pdr_override()

from sklearn.linear_model import LinearRegression, Ridge, LogisticRegression
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import metrics

"""**Importing** **Data**"""

from google.colab import files
uploaded = files.upload()

import io

df_full =  pd.read_csv(io.BytesIO(uploaded['NTDOY.csv']))

"""**checking the learned things**"""

df_full.shape

df_full.describe()   #this is cool

df_full["Adj Close"].plot()

df_full.isnull().any()

df_full.head()

"""**DATA PREPROCESSING**"""

df_full.set_index("Date", inplace=True)

df_full.head()

w_size = 30
num_of_samples = len(df_full)-w_size
indices=np.arange(num_of_samples).astype(np.int)[:,None]+np.arange(w_size+1).astype(np.int)
data = df_full['Adj Close'].values[indices]
x = data[:,:-1] 
y = data[:,-1]

split_fraction=0.8
ind_split=int(split_fraction*num_of_samples)

x_train = x[:ind_split]
y_train = y[:ind_split]
x_test = x[ind_split:]
y_test = y[ind_split:]

"""**modelling**"""

def get_performance (model_pred):
  
  print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, model_pred).round(4))  
  print('Mean Squared Error:', metrics.mean_squared_error(y_test, model_pred).round(4))  
  print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, model_pred)).round(4))

def get_plot (model_pred):
  plt.scatter(model_pred, y_test, color="blue")
  plt.plot(y_test, y_test, color='red', linewidth=2)

"""**base data**"""

y_pred_lag=np.roll(y_test,1)

get_performance(y_pred_lag)

get_plot(y_pred_lag)



"""**LINEAR REGRESSION**"""

model_lr=LinearRegression()
model_lr.fit(x_train, y_train)

y_pred_lr=model_lr.predict(x_test)

get_performance(y_pred_lr)

get_plot(y_pred_lr)



"""**Ridge Regression**"""

model_ridge = Ridge()
model_ridge.fit(x_train, y_train)

y_pred_ridge=model_ridge.predict(x_test)

get_performance(y_pred_ridge)

get_plot(y_pred_ridge)



