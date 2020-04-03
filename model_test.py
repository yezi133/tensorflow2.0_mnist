import tensorflow as tf
import numpy as np

mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
test_images = test_images.reshape(10000, 28, 28, 1)
test_images = test_images/255.0

model = tf.keras.models.load_model('model/mnist_cnn.h5')
model.summary()

# 测试模型的准确率
loss, acc = model.evaluate(test_images, test_labels)
print('模型的测试准确率为{}'.format(acc))