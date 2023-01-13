# Identifying Ripe Fruit using Hyperspectral Imagery
 
Hyperspectral cameras record the chemical composition of a fruit through visible and near-infrared wavelengths, 
therefore being far more accurate in the process of predicting the ripeness levels of a fruit compared to the 
classical RGB camera. But as with any new technology, hyperspectral imaging is still expensive and not always 
accessible to small farms.

This project introduces two classification algorithms of ripening fruit images using deep learning 
methods. More precisely, one performs supervised classification of RGB images of fresh and 
rotten fruit in comparison to a second algorithm that identifies and evaluates similar features of 
hyperspectral images to conclude if the two methods reach comparable results.

The main aspects for the hyperspectral analysis were the visualisation of the dataset and the 
implementation of Principal Component Analysis. In addition, the variation of brightness values 
throughout the spectral bands was studied in order to observe the alterations induced by the 
ripening process. Next, principal component analysis was employed to select the most 
informative of wavelengths as a method of dimensionality reduction and feature selection.
For training purposes, for both the RGB and the hyperspectral dataset, Convolutional Neural 
Network architectures that best fit the characteristics of the datasets were developed.

While hyperspectral cameras and machine learning algorithms have a wide range of applications, 
the goal of the project is to compare the behaviour of the two approaches and the particularities 
of their performance as well as to conclude if the results are subject to change based on the fruit 
used in the analysis.

For this project, Python programming language was used, including Spectral Python for hyperspectral 
images loading, visualisation and for the execution of principal component analysis, whilst Matplotlib 
was used for graphs display. Tensorflow and Keras were employed for the learning algorithm and 
classification part of the project and OpenCV was chosen for importing and displaying the RGB images.

#### Hyperspectral image of avocado classified as "unripe"

![hsi_img_avoacado](https://user-images.githubusercontent.com/122640467/212420487-b1ffa17b-29f3-4d3b-9f3b-b3bbec5c0f40.png)

#### RGB image of avocado classified as "unripe"

![rgb_img_avocado](https://user-images.githubusercontent.com/122640467/212420533-21122d10-499c-47f6-94de-b22820b4071f.png)
