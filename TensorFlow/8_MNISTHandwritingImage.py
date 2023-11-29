import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist
# MNIST 데이터셋 임포트 from TensorFlow
# => x_train, x_test = 28×28 픽셀의 각 손글씨 이미지 데이터
# => y_train, y_test = 분류에 사용되는 0~9 사이의 레이블 값
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 데이터 전처리
# => 0 ~ 255.0 pixels to 0 ~ 1.0 pixels 
x_train, x_test = x_train/255.0, x_test/255.0

# 모델 구성
# => Input layer에서 Flatten()을 이용해서 28×28 픽셀의 값을 784개의 1차원 배열로 변환
# => 각 층은 512개와 10개의 인공 뉴런 노드를 갖고 각각 ReLU (tf.nn.relu)와 소프트맥스 (tf.nn.softmax) 사용
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

# 모델 컴파일
# => optimizer : Adam (Adaptive Momentum estimation) to minimize value from Loss function
# => Loss function : sparse_categorical_crossentropy
# => metrics : accuracy
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 훈련
# model.fit(x_train, y_train, epochs=5)

# test_loss, test_acc = model.evaluate(x_test, y_test)
# print('테스트 정확도:', test_acc)

# 정확도 평가
loss, accuracy = [], []
for i in range(10):
    model.fit(x_train, y_train, epochs=1)
    loss.append(model.evaluate(x_test, y_test)[0])
    accuracy.append(model.evaluate(x_test, y_test)[1])


print(accuracy)
