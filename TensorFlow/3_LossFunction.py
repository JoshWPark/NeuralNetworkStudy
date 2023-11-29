import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.Sequential([keras.layers.Dense(units=3, input_shape=[1])])
# 손실함수는 Neural Network의 예측이 얼마나 잘 맞는지 측정하는 역할
# mse = Mean Squared Error = 평균 제곱 오차를 계산 (can be different loss function)
model.compile(loss='mse')
pred = model.predict([0])
print(pred)
# Neural Network 손실 계산
# => evaluate() 메서드를 호출하면 손실 값 (loss)을 출력
model.evaluate([0],[[0,1,0]])