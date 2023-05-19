# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 07:35:17 2023

@author: USER
"""

from flask import Flask, render_template, request, jsonify
import json
import numpy as np
from joblib import load

app = Flask(__name__)

# Load the trained KNN model
model = load('knn_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load the input data from the form and convert it to a numpy array
    data = np.array(list(request.get_json().values())).astype(float)

    # Scale the input data to a range of 0 to 4
    scaled_data = data / 4

    # Make the prediction using the trained KNN model
    prediction = model.predict(scaled_data.reshape(1, -1))

    # Convert the prediction to a boolean value indicating whether the person is divorced
    is_divorced = bool(prediction)

    return jsonify(divorced=is_divorced)

if __name__ == '__main__':
    app.run(debug=True)
