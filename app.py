import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

titanic_df = pd.read_csv("titanic.csv")

titanic_df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

titanic_df['Sex'] = titanic_df['Sex'].map({'male': 0, 'female': 1})
titanic_df['Embarked'] = titanic_df['Embarked'].map({'S':0, 'C': 1, 'Q': 2})

titanic_df['Age'] = titanic_df['Age'].fillna({'Age': titanic_df['Age'].mean()})

X = titanic_df.drop('Survived', axis=1)
Y = titanic_df['Survived']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42 )

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)

rfc = RandomForestClassifier(n_estimators=100, random_state=42)

rfc.fit(x_train_scaled, Y_train)

y_pred = rfc.predict(x_test_scaled)

def predictSurvival(sex, pcl, age, sibsp, parch, fare, embarked):
    new_passenger = pd.DataFrame({
        'Pclass': [pcl],
        'Sex': [sex],
        'Age': [age],
        'SibSp': [sibsp],
        'Parch': [parch],
        'Fare': [fare],
        'Embarked': [embarked]
    })
    
    new_passenger_scaled = scaler.transform(new_passenger)
    
    prediction = rfc.predict(new_passenger_scaled)
    return prediction[0]




