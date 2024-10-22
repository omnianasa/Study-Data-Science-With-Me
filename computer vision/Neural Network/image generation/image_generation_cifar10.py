# import main libraries will be used
import cv2
import numpy as np
from tensorflow.keras import models, layers, datasets
import matplotlib.pyplot as plt

#loading the data named cifar1
# train test splitting of the data with featires and labels
(train_features, train_label), (test_feature, test_label) = datasets.cifar10.load_data()
 
# convert the arrays of images in scale 0 to 1 otherwise 255
train_features , test_feature = train_features /255,  test_feature /255

# type the labels output into a list with the same index
labels = ["Plane", "Car", "Bird", "Cat", "Deer", "Dog", "Frog", "Horse", "Ship", "Truck"]


# take part of the training features, labes and testing eatures and labels
# it takes less time to train the model

train_features = train_features[:22000]
train_label = train_label[:22000]
test_feature = test_feature[:5000]
test_label = test_label[:5000]

#Building the model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = (32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation = 'relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation = 'relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation = 'relu'))
model.add(layers.Dense(10, activation = 'softmax'))

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(train_features, train_label, epochs = 10, validation_data = (test_feature, test_label))

loss, accuracy = model.evaluate(test_feature, test_label)

print("Accuracy: " , accuracy)
print("LOSS: " , loss)

model.save("image_classifier.h5")



