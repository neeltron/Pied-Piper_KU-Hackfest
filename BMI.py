# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 22:34:27 2021

@author: Neel
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

weight = float(input("Enter your weight in KGs: "))
height = float(input("Enter your height in metres: "))
bmi = weight / height**2
print(bmi)

df = pd.read_csv('Datasets/stroke.csv')

df=df.drop(columns='id',axis=1)
df.fillna(df.mode())
df=df.dropna()

df.gender.replace({'Male': 1, 'Female': 0, "Other": 2}, inplace=True)

df.ever_married.replace({'No': 0, 'Yes': 1}, inplace=True)

df.work_type.replace({'Private': 0, 'Self-employed': 1, 'children': 2,'Govt_job':3,'Never_worked':4}, inplace=True)

df.Residence_type.replace({'Urban': 0, 'Rural': 1}, inplace=True)

df.smoking_status.replace({'never smoked': 0, 'Unknown': 1,'formerly smoked':2,'smokes':3}, inplace=True)

X = df.drop(columns=["stroke"])
y = df["stroke"]

from sklearn.model_selection import train_test_split
#Splitting data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=44, shuffle =True)

from sklearn.ensemble import GradientBoostingClassifier

#Applying GradientBoostingClassifier Model 


GBCModel = GradientBoostingClassifier(n_estimators=100,max_depth=3,random_state=33) 
GBCModel.fit(X_train, y_train)

#Calculating Details
print('GBCModel Train Score is : ' , GBCModel.score(X_train, y_train))
print('GBCModel Test Score is : ' , GBCModel.score(X_test, y_test))
#print('----------------------------------------------------')

#Calculating Prediction
y_pred = GBCModel.predict(X_test)
y_pred_prob = GBCModel.predict_proba(X_test)
