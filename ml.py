import tensorflow as tf
import numpy as np
from tensorflow import keras

model = tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])

model.compile(optimizer='sgd',loss='mean_squared_error')

x = np.array([1,2,3,4],dtype=int)

y = np.array([1,4,6,8],dtype=int)

model.fit(x,y,epochs=500)

print(model.predict(np.array([5])))




























# model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# model.compile(optimizer='sgd', loss='mean_squared_error')

# xs = np.array([1.0, 4.0, 5.0, 2.0, 3.0, 6.0], dtype=float)
# ys = np.array([2.0, 8.0, 10.0, 4.0, 6.0, 12.0], dtype=float)

# model.fit(xs, ys, epochs=500)  

# print(model.predict(np.array([10.0])))