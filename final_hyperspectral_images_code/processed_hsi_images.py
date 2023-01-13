from spectral import *
import spectral.io.envi as envi
from spectral import principal_components
import matplotlib.pyplot as plt
import os
from pathlib import Path
list_of_eigenvalues = []

# In the function below Principal Component Analysis
# is implemented on the image offered as parameter
# The number of principal components is reduced to three
# In the end the reduced components transform the input
# image and the function returns it


def compute_pca(image):
    pc = principal_components(image)
    v = pc.cov
    # print(v)
    pc_reduced = pc.reduce(num=3)
    # print("How many eigenvalues are left: ", len(pc_reduced.eigenvalues))
    # print("How many eigenvectors are left: ", len(pc_reduced.eigenvectors))
    # print("eigenvalues: ", pc_reduced.eigenvalues)
    img_pc = pc_reduced.transform(image)
    # print("img_pc type is ", type(img_pc))
    # imshow(img_pc[:, :, :len(pc_reduced.eigenvalues)], stretch_all=True)
    # plt.pause(5)
    return img_pc


# In the function below the hyperspectral images
# are converted to RGB, using the get_rgb()
# Spectral Python function


def rgb_image_conversion(path_from_file, path_to_class, image_name, rgb_channels):
    img_header = envi.open('%s%s.hdr' % (path_from_file, image_name), '%s%s.bin' % (path_from_file, image_name))
    img_data = img_header.load()
    rgb_img = get_rgb(img_data, rgb_channels)
    # imshow(rgb_img)
    # plt.waitforbuttonpress()
    save_rgb('%s%s.png' % (path_to_class, image_name), rgb_img, format='png')

# The parameters attributed to the variables below
# are spectral bands that will form
# the unripe, ripe and overripe images
# The first wavelength refers to the Red color
# The second to the Green component
# The last determines the Blue color
# They have been selected differently
# in order to show the images as natural as possible


rgb_values_for_unripe_fruit = [30, 60, 80]
rgb_values_for_ripe_fruit = [40, 50, 70]
rgb_values_for_overripe_fruit = [40, 79, 103]

path_to_unripe_class = "E:\\hsi_dataset_files\\Avocado_version_2\\rgb_images_with_labels\\unripe\\"
path_to_ripe_class = "E:\\hsi_dataset_files\\Avocado_version_2\\rgb_images_with_labels\\ripe\\"
path_to_overripe_class = "E:\\hsi_dataset_files\\Avocado_version_2\\rgb_images_with_labels\\overripe\\"

path_to_unripe_class_PCA = "E:\\hsi_dataset_files\\Avocado_version_2\\pca_reduced_images_with_labels\\unripe\\"
path_to_ripe_class_PCA = "E:\\hsi_dataset_files\\Avocado_version_2\\pca_reduced_images_with_labels\\ripe\\"
path_to_overripe_class_PCA = "E:\\hsi_dataset_files\\Avocado_version_2\\pca_reduced_images_with_labels\\overripe\\"

# read_image_training("avocado_day_01_15_front")

# The images are exported as RGB
# To folders named after the class they belong to


def export_rgb_images(source_directory, path_to_file, path_to_class, rgb_values):
    base_path = Path(__file__).parent
    paths = (base_path / source_directory).glob('**/*')
    files = [x for x in paths if x.is_file()]
    for i in range(len(files)):
        image_name = files[i].stem
        rgb_image_conversion(path_to_file, path_to_class, image_name, rgb_values)

# The images are saved in png file formats after
# the principal components have been selected
# Each image is then saved in a folder named after the
# class it belongs to


def export_pca_reduced_images(source_directory, path_to_file, path_to_class):
    base_path = Path(__file__).parent
    paths = (base_path / source_directory).glob('**/*')
    files = [x for x in paths if x.is_file()]
    for i in range(len(files)):
        image_name = files[i].stem
        image_header = envi.open("%s%s.hdr" % (path_to_file, image_name), "%s%s.bin" % (path_to_file, image_name))
        compute_pca(image_header)
        save_rgb('%s%s.png' % (path_to_class, image_name), compute_pca(image_header), format="png")


export_pca_reduced_images("E:\\hsi_dataset_files\\Avocado_version_2\\hyperspectral_images_with_labels\\unripe",
                          "E:\\hsi_dataset_files\\Avocado_version_2\\hyperspectral_images_with_labels\\unripe\\",
                          path_to_unripe_class_PCA)

export_pca_reduced_images("E:\\hsi_dataset_files\\Avocado_version_2\\hyperspectral_images_with_labels\\ripe",
                          "E:\\hsi_dataset_files\\Avocado_version_2\\hyperspectral_images_with_labels\\ripe\\",
                          path_to_ripe_class_PCA)

export_pca_reduced_images("E:\\hsi_dataset_files\\Avocado_version_2\\hyperspectral_images_with_labels\\overripe",
                          "E:\\hsi_dataset_files\\Avocado_version_2\\hyperspectral_images_with_labels\\overripe\\",
                          path_to_overripe_class_PCA)

export_rgb_images("E:\\hsi_dataset_files\\Avocado_version_2\\hyperspectral_images_with_labels\\unripe",
                  "E:\\hsi_dataset_files\\Avocado_version_2\\hyperspectral_images_with_labels\\unripe\\",
                  path_to_unripe_class, rgb_values_for_unripe_fruit)
export_rgb_images("E:\\hsi_dataset_files\\Avocado_version_2\\hyperspectral_images_with_labels\\ripe",
                  "E:\\hsi_dataset_files\\Avocado_version_2\\hyperspectral_images_with_labels\\ripe\\",
                  path_to_ripe_class, rgb_values_for_ripe_fruit)
export_rgb_images("E:\\hsi_dataset_files\\Avocado_version_2\\hyperspectral_images_with_labels\\overripe",
                  "E:\\hsi_dataset_files\\Avocado_version_2\\hyperspectral_images_with_labels\\overripe\\",
                  path_to_overripe_class, rgb_values_for_overripe_fruit)
# ----------------------------------------------------------------------------------------------------------
