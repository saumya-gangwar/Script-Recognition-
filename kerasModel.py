# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:12:24 2019

@author: SAUMYA

Keras Model For Character Recognition
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory


# Any results you write to the current directory are saved as output.

data=pd.read_csv("data1.csv")
print(data.shape)
X=data.iloc[:,:-1]
Y=data.iloc[:,-1]
#print(X[].head(200))
Y=Y.values.reshape(92000,1)
#print(X.shape)
X=X.values.reshape(X.shape[0],32,32,1)
print("Done")

from sklearn.preprocessing import LabelBinarizer
binencoder = LabelBinarizer()
Y= binencoder.fit_transform(Y)
print("done")

from sklearn.model_selection import train_test_split
xTrain,xTest,yTrain,yTest=train_test_split(X,Y,test_size=0.2,shuffle=True)

print(xTrain.shape)
print(yTrain.shape)

import tensorflow
import keras
from numpy import array
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

model=Sequential()
model.add(Conv2D(42,(3,3),input_shape=(32,32,1),activation='relu',padding='same'))
model.add(Flatten())
model.add(Dense(units=32 ,activation='relu',kernel_initializer="uniform"))
model.add(Dense(units=46, activation='softmax', kernel_initializer='uniform'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.summary()
model.fit(xTrain, yTrain, batch_size=32, epochs=10, shuffle=True,class_weight=None, sample_weight=None, callbacks=[],validation_data=(xTest,yTest))
model.save("model.h5")