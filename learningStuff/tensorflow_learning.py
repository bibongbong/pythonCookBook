import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)


#从Tensorflow直接访问Fashion MNIST，导入和加载数据
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels),(test_images, test_labels) = fashion_mnist.load_data()

'''
Fashion MNIST 数据集，其中包含 70000 张单件服饰的灰度图像，涵盖 10 个类别。
较低分辨率（28x28 像素） 每张图都映射到一个标签，由于数据集不包含类别名词，所以用class_names来存储
0	T 恤衫/上衣
1	裤子
2	套衫
3	裙子
4	外套
5	凉鞋
6	衬衫
7	运动鞋
8	包包
9	踝靴
'''
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print(train_images.shape) # (60000, 28, 28)  表示训练集中有60000张图片，每张像素28x28
print(len(train_labels))  # 60000 :表示60000个标签
print(train_labels) 	# [9 0 0 ... 3 0 5]


# 每张图的像素值介于0-255之间
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()	# 显示色彩对比栏
#plt.grid(False)
#plt.show()	# 显示图像


# 先对数据预处理，在训练网络
# 我们将这些值缩小到0-1之间，然后将其馈送到神经网络模型
train_images = train_images / 255.0
test_images = test_images / 255.0

# 显示训练集中的前25张图片，并显示类别名称
plt.figure(figsize=(10,10)) # 设置每张图的大小 10x10
for i in range(25):
	plt.subplot(5, 5, i+1)	# 设置25张图片的排位，行数x列数
	plt.xticks([])
	plt.yticks([])
	plt.grid(True)
	plt.imshow(train_images[i], cmap=plt.cm.binary)
	plt.xlabel(class_names[train_labels[i]])

#plt.show()


'''
构建模型
1. 设置层
该网络中的第一层  tf.keras.layers.Flatten 将图像格式从二维数组（28x28 像素）转换成一维数组（28 * 28 = 784 像素）
在扁平化像素之后，该网络包含两个 tf.keras.layers.Dense 层的序列。这些层是密集连接或全连接神经层。
第一个 Dense 层具有 128 个节点（或神经元）
第二个（也是最后一个）层是具有 10 个节点的 softmax 层，该层会返回一个具有 10 个概率得分的数组，这些得分的总和为 1。
每个节点包含一个得分，表示当前图像属于 10 个类别中某一个的概率。
'''
model = keras.Sequential([
	keras.layers.Flatten(input_shape=(28, 28)),
	keras.layers.Dense(128, activation=tf.nn.relu),
	keras.layers.Dense(10, activation=tf.nn.softmax)
	])



'''
2. 编译模型
	a. 损失函数: 衡量模型在训练期间的准确率。我们希望尽可能缩小该函数，以“引导”模型朝着正确的方向优化。
	b. 优化器: 根据模型看到的数据及其损失函数更新模型的方式。
	c. 指标: 用于监控训练和测试步骤。以下示例使用准确率，即图像被正确分类的比例。
'''
model.compile(optimizer=tf.train.AdamOptimizer(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])



'''
3. 训练模型
	a. 将训练数据馈送到模型中，在本示例中为 train_images 和 train_labels 数组。
	b. 模型学习将图像与标签相关联。
	c. 我们要求模型对测试集进行预测，在本示例中为 test_images 数组。我们会验证预测结果是否与 test_labels 数组中的标签一致。

	epochs 是迭代次数
	在模型训练期间，系统会显示损失和准确率指标。该模型在训练数据上的准确率达到 0.89（即 89%）
'''
model.fit(train_images, train_labels, epochs=5)


'''
4. 评估准确率
Test accuracy: 0.8735

模型在测试数据集上的准确率略低于在训练数据集上的准确率。
训练准确率和测试准确率之间的这种差异表示出现过拟合。
如果机器学习模型在新数据上的表现不如在训练数据上的表现，就表示出现过拟合。

'''
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Test accuracy:", test_acc)