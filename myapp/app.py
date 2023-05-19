# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 07:35:17 2023

@author: USER
"""

from flask import Flask, render_template, request, jsonify
import numpy as np
from joblib import load

app = Flask(__name__, template_folder='templates')

# Load the trained KNN model
model = load('knn_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load input data from the form and convert it to a numpy array
    data = np.array(list(request.get_json().values())).astype(float)

    # Scale input data to the range 0 to 4
    scaled_data = data / 4

    # Predict using a trained KNN model
    prediction = model.predict(scaled_data.reshape(1, -1))

    # Convert the prediction to a boolean value indicating whether the person is divorced or not
    is_divorced = bool(prediction)

    return jsonify(divorced=is_divorced)

if __name__ == '__main__':
    app.run(debug=True)

