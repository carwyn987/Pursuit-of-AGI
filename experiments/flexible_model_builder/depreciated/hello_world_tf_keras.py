import numpy as np
import keras
from keras import layers
from keras import ops

"""
https://keras.io/guides/functional_api/

The Keras functional API is a way to create models that are more flexible than the keras.Sequential API. The functional API can handle models with non-linear topology, shared layers, and even multiple inputs or outputs.
"""

x = np.array([1, 2, 3])
y = keras.ops.convert_to_tensor(x)

inputs = keras.Input(shape=(784,))

# Just for demonstration purposes.
img_inputs = keras.Input(shape=(32, 32, 3))

print(inputs.shape)

print(inputs.dtype)

dense = layers.Dense(64, activation="relu")
x = dense(inputs)

x = layers.Dense(64, activation="relu")(x)
outputs = layers.Dense(10)(x)

model = keras.Model(inputs=inputs, outputs=outputs, name="mnist_model")

model.summary()

# keras.utils.plot_model(model, "my_first_model.png")
# keras.utils.plot_model(model, "my_first_model_with_shape_info.png", show_shapes=True)

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train.reshape(60000, 784).astype("float32") / 255
x_test = x_test.reshape(10000, 784).astype("float32") / 255

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.RMSprop(),
    metrics=["accuracy"],
)

history = model.fit(x_train, y_train, batch_size=64, epochs=2, validation_split=0.2)

test_scores = model.evaluate(x_test, y_test, verbose=2)
print("Test loss:", test_scores[0])
print("Test accuracy:", test_scores[1])
