# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 15:34:27 2021

@author: Neel
"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import sklearn.metrics
from sklearn import datasets
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
import os
import mysql.connector

def databasefetcher(username):
    db = mysql.connector.connect(
        host="remotemysql.com",
        user="hwW4R6cA0s",
        passwd="9bVe4xsxvX",
        db="hwW4R6cA0s"
    )
    cursor = db.cursor()
    sql = "SELECT * FROM input WHERE username = %s"
    val = (username, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    return result[0]

def heart_rf(age, sex, anaemia, bp, diabetes, smoking, time):
    os.environ['PATH'] = os.environ['PATH']+';'+os.environ['CONDA_PREFIX']+r"\Library\bin\graphviz"
    data = pd.read_csv("Datasets/heart_failure.csv")
    predictors = data[["age", "anaemia", "diabetes", "high_blood_pressure", "sex", "smoking", "time"]]
    targets = data.DEATH_EVENT
    pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size = .4, random_state = 2)
    classifier = RandomForestClassifier(n_estimators = 400)
    classifier = classifier.fit(pred_train, tar_train)
    predictions = classifier.predict(pred_test)
    accuracy = sklearn.metrics.accuracy_score(tar_test, predictions)
    model = ExtraTreesClassifier()
    model.fit(pred_train, tar_train)
    lst = []
    lst.append(classifier.predict([[age, anaemia, diabetes, bp, sex, smoking, time]]))
    lst.append(accuracy*100)
    return lst

input_tuple = databasefetcher("neeltron")
username = input_tuple[0]
age = input_tuple[1]
sex = input_tuple[8]
anaemia = input_tuple[5]
bp = input_tuple[7]
diabetes = input_tuple[6]
smoking = input_tuple[9]
time = input_tuple[10]

print(heart_rf(age,sex,anaemia, bp, diabetes, smoking, time))
