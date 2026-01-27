# Day-6 Deep Learning: Simple Neural Network

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Load data
data = load_iris()
X = data.data
y = data.target.reshape(-1,1)

# One-hot encode target
encoder = OneHotEncoder(sparse=False)
y = encoder.fit_transform(y)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build model
model = Sequential()
model.add(Dense(16, activation='relu', input_shape=(4,)))
model.add(Dense(16, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compile
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train
model.fit(X_train, y_train, epochs=50, verbose=0)

# Evaluate
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print("Neural Network Accuracy:", acc)
