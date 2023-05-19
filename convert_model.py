# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 07:32:30 2023

@author: USER
"""

import onnx
import skl2onnx
from joblib import load
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# Load scikit-learn model
knn_model = load("knn_model.joblib")

# Define input data type
initial_type = [('float_input', FloatTensorType([None, 54]))]

# Convert scikit-learn model to ONNX
onnx_model = convert_sklearn(knn_model, initial_types=initial_type)

# Save the ONNX model
with open("knn_model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())
