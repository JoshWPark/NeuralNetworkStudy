import tensorflow as tf
import numpy as np

tf.random.set_seed(0)

# 훈련 데이터 준비하기
x_train = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
y_train = np.array([[0], [1], [1]])

# 뉴런층 만들기
input_layer = tf.keras.layers.InputLayer(input_shape=(3,))
hidden_layer = tf.keras.layers.Dense(units=4, activation='relu')
output_layer = tf.keras.layers.Dense(units=2, activation='softmax')

# 모델 구성하기
model = tf.keras.Sequential([
  input_layer,
  hidden_layer,
  output_layer
  ])

# 모델 컴파일하기
model.compile(loss='mse', optimizer='Adam')

# 은닉층의 출력 확인하기
# => tf.keras 모듈의 Model 클래스를 사용해서 새로운 모델 (intermediate_layer_model)을 생성
# => 앞에서 구성한 전체 모델의 입력을 입력으로 하고 첫번째 뉴런층 (hidden_layer)의 출력을 출력으로 하는 신경망 모델.
# => 이 모델에 훈련 데이터 (x_train)을 입력하면 첫번째 뉴런층의 출력을 반환.
intermediate_layer_model = tf.keras.Model(inputs=model.input, outputs=model.layers[0].output)
intermediate_output = intermediate_layer_model(x_train)

print('======== Inputs ========')
print(x_train)

print('\n======== Weights of Hidden Layer ========')
print(hidden_layer.get_weights()[0])

print('\n======== Outputs of Hidden Layer ========')
print(intermediate_output)

# 출력층의 출력 확인하기
# => predict() 를 사용하여 전체 신경망의 출력값 반환.
pred = model.predict(x_train)

print('\n======== Outputs of Output Layer ========')
print(pred)