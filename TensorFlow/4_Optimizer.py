import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('default')
plt.rcParams['figure.figsize'] = (4, 3)
plt.rcParams['font.size'] = 12
# 랜덤 시드 설정
tf.random.set_seed(0)
model = keras.Sequential([keras.layers.Dense(units=3, input_shape=[1], use_bias=False)])

tf.random.set_seed(0)
model2 = tf.keras.models.clone_model(model)

tf.random.set_seed(0)
model3 = tf.keras.models.clone_model(model)

# 옵티마이저는 더 개선된 예측값을 출력하도록 최적화하는 알고리즘
# SGD = Stochastic Gradient Descent = 확률적 경사하강법 (can be different optimizer)
# model.compile(loss='mse', optimizer='SGD')

# history = model.fit([1], [[0, 1, 0]], epochs=100)

# 손실값 시각화하기
# plt.style.use('default')
# plt.rcParams['figure.figsize'] = (4, 3)
# plt.rcParams['font.size'] = 12

# loss = history.history['loss']
# plt.plot(loss)
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.show()

# 옵티마이저 비교
model.compile(loss='mse', optimizer='SGD')
model2.compile(loss='mse', optimizer='Adam')
model3.compile(loss='mse', optimizer='RMSprop')

history = model.fit([1], [[0, 1, 0]], epochs=100, verbose=0)
history2 = model2.fit([1], [[0, 1, 0]], epochs=100, verbose=0)
history3 = model3.fit([1], [[0, 1, 0]], epochs=100, verbose=0)

loss = history.history['loss']
loss2 = history2.history['loss']
loss3 = history3.history['loss']
plt.plot(loss, label='SGD')
plt.plot(loss2, label='Adam')
plt.plot(loss3, label='RMSprop')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc='lower left')
plt.show()