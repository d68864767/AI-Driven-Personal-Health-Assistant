```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class AIModel:
    def __init__(self, input_dim):
        self.model = Sequential()
        self.model.add(Dense(32, input_dim=input_dim, activation='relu'))
        self.model.add(Dense(16, activation='relu'))
        self.model.add(Dense(1, activation='sigmoid'))

    def compile_model(self):
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    def train_model(self, X, y, epochs=10, batch_size=32):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_test, y_test))

    def predict(self, X):
        return self.model.predict(X)
```
