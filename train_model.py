import numpy as np
import pandas as pd
import pickle

df = pd.read_csv('Titanic-Dataset.csv')

# Handling missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df.isnull().sum())

# feature selection
x = df[["Pclass", "Sex", "Age", "Fare", "Embarked", "SibSp", "Parch"]]
y = df["Survived"]
x = pd.get_dummies(x, columns=["Sex", "Embarked"])
print(x)
print(y)

# Fitting model
from sklearn.linear_model import LogisticRegression

log_model = LogisticRegression(max_iter=1000)

log_model.fit(x, y)

y_pred = log_model.predict(x)

print("Prediction on training set:", y_pred)

print("Accuracy on training set:", log_model.score(x, y))

pickle.dump(log_model, open("titanic_model.pkl", "wb"))