import cv2
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------
# Histogram of UNRIPE Avocado
# ----------------------------------------
image_1 = cv2.imread('E:\\hsi_dataset_files\\Avocado_version_2\\test images\\avocado_day_01_22_front.png')

color = ('b', 'g', 'r')
for channel, col in enumerate(color):
    histogram = cv2.calcHist([image_1], [channel], None, [256], [0, 256])
    plt.plot(histogram, color=col)
    plt.xlim([0, 256])
    plt.ylim([0, 1700])
plt.title('Histogram of Unripe Avocado')
plt.savefig("unripe_avocado_histogram.png")
plt.show()

# ----------------------------------------
# Histogram of RIPE Avocado
# ----------------------------------------
image_2 = cv2.imread('E:\\hsi_dataset_files\\Avocado_version_2\\test images\\avocado_day_05_04_front.png')

color = ('b', 'g', 'r')
for channel, col in enumerate(color):
    histogram = cv2.calcHist([image_2], [channel], None, [256], [0, 256])
    plt.plot(histogram, color=col)
    plt.xlim([0, 256])
    plt.ylim([0, 1700])
plt.title('Histogram of Ripe Avocado')
plt.savefig("ripe_avocado_histogram.png")
plt.show()

# ----------------------------------------
# Histogram of OVERRIPE Avocado
# ----------------------------------------
image_3 = cv2.imread('E:\\hsi_dataset_files\\Avocado_version_2\\test images\\avocado_day_10_04_front.png')

color = ('b', 'g', 'r')
for channel, col in enumerate(color):
    histogram = cv2.calcHist([image_3], [channel], None, [256], [0, 256])
    plt.plot(histogram, color=col)
    plt.xlim([0, 256])
    plt.ylim([0, 2000])
plt.title('Histogram of Overripe Avocado')
plt.savefig("overripe_avocado_histogram.png")
plt.show()

# -----------------------------------------
# Gray Scale histogram UNRIPE Avocado
# -----------------------------------------
image_1_grayscale = cv2.imread('E:\\hsi_dataset_files\\Avocado_version_2\\test images\\avocado_day_01_22_front.png',
                      cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([image_1_grayscale], [0], None, [256], [0, 256])
plt.hist(image_1_grayscale.ravel(), 256, [0, 256])
plt.title('Histogram for gray scale unripe avocado')
plt.savefig("gray_scale_histogram_unripe_avocado.png")
plt.show()

# -----------------------------------------
# Gray Scale histogram RIPE Avocado
# -----------------------------------------
image_2_grayscale = cv2.imread('E:\\hsi_dataset_files\\Avocado_version_2\\test images\\avocado_day_05_04_front.png',
                      cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([image_2_grayscale], [0], None, [256], [0, 256])
plt.hist(image_2_grayscale.ravel(), 256, [0, 256])
plt.title('Histogram for gray scale ripe avocado')
plt.savefig("gray_scale_histogram_ripe_avocado.png")
plt.show()

# -----------------------------------------
# Gray Scale histogram OVERRIPE Avocado
# -----------------------------------------

image_3_grayscale = cv2.imread('E:\\hsi_dataset_files\\Avocado_version_2\\test images\\avocado_day_10_04_front.png',
                      cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([image_3_grayscale], [0], None, [256], [0, 256])
plt.hist(image_3_grayscale.ravel(), 256, [0, 256])
plt.title('Histogram for gray scale overripe avocado')
plt.savefig("gray_scale_histogram_overripe_avocado.png")
plt.show()
