#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import module
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import cv2

#import data in tensorflow directory
mnist = tf.keras.datasets.mnist
(x_train,y_train) , (x_test, y_test) = mnist.load_data()

#normalize data
x_train = tf.keras.utils.normalize(x_train,axis=1)
x_test = tf.keras.utils.normalize(x_test,axis=1)

#make layers
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape =(28,28)))
model.add(tf.keras.layers.Dense(128, activation ='relu'))
model.add(tf.keras.layers.Dense(128, activation ='relu'))
model.add(tf.keras.layers.Dense(10, activation ='softmax'))

#train model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train,epochs=3)

#check loss and accuracy
loss, accuracy = model.evaluate(x_test, y_test)
print(loss)
print(accuracy)

#with this model i got (loss: 0.1113 and accuracy: 0.9665) as you can see in below
313/313 [==============================] - 0s 966us/step - loss: 0.1113 - accuracy: 0.9665
0.11129797250032425
0.9664999842643738

#look for the file that you have created and want to predict in my case i put in folder nmistnumber/number
image_number = 1
while os.path.isfile(f"nmistnumber/number{image_number}.png"):
    try:
        img = cv2.imread(f"nmistnumber/number{image_number}.png") [:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print (f"angka ini adalah {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except:
        print("error")
    finally:
        image_number += 1

