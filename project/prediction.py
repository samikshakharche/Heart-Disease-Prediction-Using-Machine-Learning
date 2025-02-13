

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics



from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('heart.csv')

x=data.drop(['target'],axis=1)
y=data['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

classifier= RandomForestClassifier()

classifier.fit(x_train,y_train)

print(x_test)
def prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    res = classifier.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if res[0]==1: res = "Yes you are likely to have a heart disease"
    else: res = "You don't have a heart disease"
    return res
     