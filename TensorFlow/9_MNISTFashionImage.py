import tensorflow as tf
import numpy as np

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
      if logs.get('loss') < 0.3:
          print('\n훈련을 중지합니다.')
          self.model.stop_training = True
callbacks = myCallback()
# Fashion MNIST 데이터셋 불러오기
# => return value : numpy array value
# => train_image, train_labels for training
# => test_image, test_lables for testing
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# 데이터 전처리
train_images, test_images = train_images / 255.0, test_images / 255.0

# 모델 구성
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 훈련
model.fit(train_images, train_labels, epochs=5, callbacks=[callbacks])

# 정확도 평가하기
loss, accuracy = model.evaluate(test_images, test_labels)
print(loss, accuracy)

# 7. 예측하기
# predictions = model.predict(test_images)
# print(predictions[0])
# print(np.argmax(predictions[0]))


# 뉴런 노드의 개수가 증가하면 훈련 과정에서 손실 값이 감소하고 테스트 정확도는 증가하는 경향이 있다
# But, 계산과 최적화를 필요로 하는 파라미터의 숫자가 증가하기 때문에 훈련에 걸리는 시간은 증가