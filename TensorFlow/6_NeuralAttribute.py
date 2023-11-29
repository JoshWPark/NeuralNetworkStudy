import tensorflow as tf

tf.random.set_seed(0)

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
 
# 뉴런층의 이름과 자료형
print(input_layer.name, input_layer.dtype)
print(hidden_layer.name, hidden_layer.dtype)
print(output_layer.name, output_layer.dtype)

# 모델 뉴런층의 이름 
# => input_layer is not part of model.layers
print(model.layers[0].name)
print(model.layers[1].name)

# 뉴런층의 입출력
# => input : input_tensor, output : output_tensor
print(input_layer.input)
print(input_layer.output)
print(hidden_layer.input)
print(hidden_layer.output)
print(output_layer.input)
print(output_layer.output)

# 뉴런층의 활성화함수 (activation)
print(hidden_layer.activation)
print(hidden_layer.activation.__name__)
print(output_layer.activation)
print(output_layer.activation.__name__)

# 뉴런층의 가중치 (weights)
print(hidden_layer.weights)
print(output_layer.weights)

# get_weights()
# => 가중치를 numpy 어레이 형식으로 
print(hidden_layer.get_weights())
print(output_layer.get_weights())