```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """
    Function to load the dataset from a specified file path.
    """
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data, target_column):
    """
    Function to preprocess the data. It separates the features and the target variable, 
    and scales the features using StandardScaler.
    """
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X, y

def save_model(model, file_path):
    """
    Function to save the trained model to a specified file path.
    """
    model.save(file_path)

def load_model(file_path):
    """
    Function to load a trained model from a specified file path.
    """
    return keras.models.load_model(file_path)
```
