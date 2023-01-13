import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow
import pathlib
import matplotlib.pyplot as plt
import numpy as np

from tensorflow import keras
from keras.layers import Rescaling, RandomFlip, Resizing, RandomRotation, RandomZoom, Conv2D, MaxPooling2D, Dense, \
    Dropout, Flatten
from tensorflow.keras.models import Sequential

gpus = tensorflow.config.experimental.list_physical_devices('GPU')

# I attribute the path to the folder with all the images to full_dataset variable
# the total number of images will be equal to 172
full_dataset = pathlib.Path('E:\\hsi_dataset_files\\Avocado_version_2\\rgb_images_with_labels')
images_total_number = len(list(full_dataset.glob('*/*.png')))
print(images_total_number)

# I declare the parameters of the data that
# will be imported into the learning model
batch_size = 20
image_height = 200
image_width = 200
epochs = 30
bands_number = 3

# train holds 70% of the entire dataset and test the rest of 30%
# image_dataset_from_directory is a function that reads the images from the folders
# The classification labels are the names of the folders the images are stored in
# which are "unripe", "ripe", "overripe"
train = tensorflow.keras.utils.image_dataset_from_directory(
    full_dataset,
    validation_split=0.3,
    subset="training",
    seed=123,
    image_size=(image_height, image_width),
    batch_size=batch_size
)

test = tensorflow.keras.utils.image_dataset_from_directory(
    full_dataset,
    validation_split=0.3,
    subset="validation",
    seed=123,
    image_size=(image_height, image_width),
    batch_size=batch_size
)

# class_names variable returns a list with the classification labels
class_names = train.class_names
print(class_names)

# data augmentation step is comprised of
# resizing the images to the parameters declared above (200 height, 200 width)
# a horizontal random flip where the image size is equal to the
# height, width and band numbers declared above
# random rotation of 0.2
# random zoom of 0.2
data_augmentation = keras.Sequential(
    [
        Resizing(image_height, image_width),
        Rescaling(1. / 255),
        RandomFlip("horizontal", input_shape=(image_height, image_width, bands_number)),
        RandomRotation(0.2),
        RandomZoom(0.2),
    ]
)

# proposed CNN model architecture
model = Sequential([

    data_augmentation,
    Conv2D(32, (3, 3), activation="relu", input_shape=(image_height, image_width, bands_number)),
    Conv2D(32, (3, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, (3, 3), activation="relu"),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.5),

    Conv2D(128, (3, 3), activation="relu"),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),
    Dense(128, activation="relu"),

    Dropout(0.5),

    Dense(len(class_names), activation="softmax")
])

# optimizer chosen is adam in model compilation step
# as there are three classification labels and each
# image belongs to exactly one class the loss chosen is
# SparseCategoricalCrossentropy

model.compile(optimizer='adam',
              loss=tensorflow.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['accuracy'])

# the model is trained on the training and validation datasets
history = model.fit(
    train,
    batch_size=batch_size,
    epochs=epochs,
    verbose=1,
    validation_data=test
)

# the model summary is displayed
model.summary()

accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

# two subplots of Training and Validation Accuracy and Loss are displayed
fig, (axes_1, axes_2) = plt.subplots(1, 2)
axes_1.plot(epochs_range, accuracy, label='Training Accuracy')
axes_1.plot(epochs_range, val_accuracy, label='Validation Accuracy')
axes_1.set_title("Training and Validation Accuracy")
axes_1.set(xlabel="Number of Epochs", ylabel="Accuracy")
axes_1.legend()

axes_2.plot(epochs_range, loss, label='Training Loss')
axes_2.plot(epochs_range, val_loss, label='Validation Loss')
axes_2.set_title("Training and Validation Loss")
axes_2.set(xlabel="Number of Epochs", ylabel="Loss")
axes_2.legend()
plt.show()

# The image which is about to be classified
# is given as input to image_prediction variable
# First, the image is turned into a numpy array
image_prediction = "E:\\hsi_dataset_files\\Avocado_version_2\\test images\\avocado_day_05_04_front.png"
img = tensorflow.keras.utils.load_img(image_prediction, target_size=(image_height, image_width))
img_array = tensorflow.keras.utils.img_to_array(img)
img_array = tensorflow.expand_dims(img_array, 0)

# The model makes a prediction based on the input image
# The accuracy of the prediction is displayed
predictions = model.predict(img_array)
score = tensorflow.nn.softmax(predictions[0])
print(
    "This image is classified as {} with a {:.2f} percent accuracy."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)