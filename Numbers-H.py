#!/bin/env python

from keras import layers
from keras import models
from keras.layers.advanced_activations import LeakyReLU
from keras.callbacks import EarlyStopping
import keras 

act = LeakyReLU(alpha=0.6)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu',
                        input_shape=(200, 200, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.Dropout(.35))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.Dropout(.35))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.Dropout(.35))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())

model.add(layers.Dense(1024))#,activation='relu'))
#model.add(layers.Dropout(.35))
model.add(act) #, activation='relu'))
model.add(layers.Dense(256, activation='relu'))
#model.add(layers.Dropout(.35))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()

from keras import optimizers

model.compile(loss='binary_crossentropy',
              optimizer=keras.optimizers.Adadelta(), #optimizers.RMSprop(lr=1e-4),
              metrics=['accuracy'])

train_dir = 'data/trainH'
validation_dir = 'data/testH'

from keras.preprocessing.image import ImageDataGenerator

# All images will be rescaled by 1./255
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        # This is the target directory
        train_dir,
        # All images will be resized to 156, 126. Size set manually, 
        #depends on data.
        target_size=(200, 200),
        color_mode="grayscale",
        batch_size=40,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        validation_dir,
        target_size=(200, 200),
        color_mode="grayscale",
        batch_size=20,
        class_mode='binary')


for data_batch, labels_batch in train_generator:
    print('data batch shape:', data_batch.shape)
    print('labels batch shape:', labels_batch.shape)
    break

stop_early = EarlyStopping(monitor="val_loss",
                            min_delta=0,
                            patience=4,
                            verbose=0,
                            mode="auto")
                            #baseline=None)

history = model.fit_generator(
      train_generator,
      steps_per_epoch=188,
      epochs=20,
      validation_data=validation_generator,
      validation_steps=32.6,
      callbacks=[stop_early])


model.save("number-opt-7.h5")
