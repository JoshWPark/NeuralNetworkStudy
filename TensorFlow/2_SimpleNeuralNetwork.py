import tensorflow as tf
from tensorflow import keras
import numpy as np

# Neural Network 구성 
# => Sequential : Neural Network의 각 층을 순서대로 쌓음.
# => Dense : (완전 연결된) 하나의 뉴런층을 구현.
# => units : 출력 노드 개수, input_shape : 입력 데이터 형태
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# Neural Network Compile
# => 모델의 학습에 필요한 손실함수 (loss function)와 옵티마이저 (optimizer)를 결정
model.compile(loss='mean_squared_error', optimizer='sgd')
# Neural Network 훈련
# => fit() : 주어진 입출력 데이터에 대해 지정한 횟수만큼 Neural Network를 훈련
# => epoch : 주어진 데이터를 한 번 훈련하는 단위
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)
model.fit(xs, ys, epochs=500)
# Neural Network 예측
# => predict() : 특정 입력에 대해 Neural Network가 출력(예측)하는 값 return
pred = model.predict([3])
print(pred)