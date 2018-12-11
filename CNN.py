from ImgPrepro import Train,Test,Valid
#import ImgPrepro
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator, array_to_img,img_to_array,load_img
from keras.layers import Conv2D,MaxPooling2D, Flatten, Dense, Dropout
import matplotlib.pyplot as plt

import tensorflow as tf

batch_size=16
dataset_size=2310#150
valid_size=889

#MODEL
#Creating Sequential class object
classifier=Sequential()
#Convoution step 1
classifier.add(Conv2D(32,(3,3),input_shape=(200,200,1),activation='relu'))
#Convoution step 2
classifier.add(Conv2D(32,(3,3),activation='relu'))
#MaxPooling step 1
classifier.add(MaxPooling2D(pool_size=(2,2)))
#Dropout layer 1
classifier.add(Dropout(0.2))

#Convoution step 3
classifier.add(Conv2D(32,(3,3),activation='relu'))
#Convoution step 4
classifier.add(Conv2D(32,(3,3),activation='relu'))
#MaxPooling step 2
classifier.add(MaxPooling2D(pool_size=(2,2)))
#Dropout layer 2
classifier.add(Dropout(0.2))

#Convoution step 5
classifier.add(Conv2D(64,(3,3),activation='relu'))
#Convoution step 6
classifier.add(Conv2D(64,(3,3),activation='relu'))
#MaxPooling step 3
classifier.add(MaxPooling2D(pool_size=(2,2)))
#Dropout layer 3
classifier.add(Dropout(0.2))

#Flattening step  Converts 3D feature maps to 1D
classifier.add(Flatten())
#Layers connecting step
classifier.add(Dense(units=1024,activation='relu'))
#Dropout layer 4
classifier.add(Dropout(0.2))
#Initialzing output layer
classifier.add(Dense(units=3,activation='softmax'))

#Compiling model
classifier.compile(optimizer = 'rmsprop', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

# Create callback for early stopping on validation loss. If the loss does
# not decrease in two consecutive tries, stop training.
callbacks = [tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=2)]

#classifier.summary()
#print(classifier.layers[0].get_config())

train=Train()
valid=Valid()
hist=classifier.fit_generator(train,steps_per_epoch=dataset_size/batch_size,epochs=20,validation_data=valid,validation_steps=160/batch_size)


classifier.save("EModel20epoch,6convu6464finalconvu1024denseneurons,2310imgsrmspropsparselowdataugrescaleintrain.h5")
print("Model Saved")
#print(type(hist))

#GRAPH PLOT
print(hist.history.keys())
plt.figure(1)#1st Window

#summarize history for accuracy
plt.subplot(211)
plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')

# summarize history for loss

plt.figure(2)#2nd Window
plt.subplot(211)
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

#classifier.save_weights('50_epochs.h5')
'''
with tf.device('/gpu:0'):

 sess=tf.Session(config=tf.ConfigProto(log_device_placement=True))

a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
# Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# Runs the op.
print(sess.run(c))
'''
