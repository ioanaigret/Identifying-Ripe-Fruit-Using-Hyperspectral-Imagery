from spectral import *
import spectral.io.envi as envi
import matplotlib.pyplot as plt
from spectral import principal_components

rgb_values_for_unripe_fruit = [30, 60, 80]
rgb_values_for_ripe_fruit = [40, 50, 70]
rgb_values_for_overripe_fruit = [40, 79, 103]


def compute_pca(image, image_name):
    pc = principal_components(image)
    v = pc.cov
    # imshow(v)
    # plt.title("Covariance matrix")
    save_rgb('%s%s.png' % (image_name, "_cov_matrix"), v, format='png')
    plt.pause(1)
    print("How many eigenvalues are before reduction: ", len(pc.eigenvalues))
    print("How many eigenvectors are before reduction: ", len(pc.eigenvectors))
    pc_reduced = pc.reduce(num=3)
    print("How many eigenvalues are left: ", len(pc_reduced.eigenvalues))
    print("eigenvalues: ", pc_reduced.eigenvalues, "\n")
    img_pc = pc_reduced.transform(image)
    imshow(img_pc[:, :, :len(pc_reduced.eigenvalues)], stretch_all=True)
    plt.title("Hyperspectral Image After PCA")
    plt.pause(3)
    return img_pc


def rgb_image_conversion(image_name, rgb_channels):
    img_header = envi.open('%s.hdr' % image_name, '%s.bin' % image_name)
    img_data = img_header.load()
    rgb_img = get_rgb(img_data, rgb_channels)
    imshow(rgb_img)
    plt.title("RGB version of image")
    plt.waitforbuttonpress()
    save_rgb('%s.png' % image_name, rgb_img, format='png')


def import_image(image_name, rgb_channel):
    img = envi.open("%s.hdr" % image_name, "%s.bin" % image_name)
    img_header = img.load()
    print("ENVI file of the image", "\n", img)
    print("Image as numpy array", "\n", img_header)
    imshow(img)
    plt.title("Initial Hyperspectral Image")
    plt.pause(3)
    pca_reduced_img = compute_pca(img, image_name)
    rgb_image_conversion(image_name, rgb_channel)
    save_rgb('%s%s.png' % (image_name, "_pca_reduced"), pca_reduced_img, format="png")
    print("-------------------------------------------------------")


import_image("VIS_avocado_day_01_01_front", rgb_values_for_unripe_fruit)
import_image("avocado_day_06_01_front", rgb_values_for_ripe_fruit)
import_image("VIS_avocado_day_10_01_front", rgb_values_for_overripe_fruit)