# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 06:38:09 2023

@author: USER
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from joblib import dump

# Load the dataset
data = pd.read_excel("C:/Users/USER/Desktop/esogü/TEZ PYTHON/divorce1.xlsx")

# Split the dataset into features and labels
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Test the model's performance
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Save the trained model
dump(knn, "knn_model.joblib")
