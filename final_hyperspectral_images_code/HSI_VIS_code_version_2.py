from spectral import *
import spectral.io.envi as envi
import matplotlib.pyplot as plt
from spectral import principal_components

# list of the bands in which the images are recorded across
# 224 in total
VIS_BANDS = [397.66, 400.28, 402.9, 405.52, 408.13, 410.75, 413.37, 416.0, 418.62, 421.24, 423.86, 426.49, 429.12,
             431.74, 434.37, 437.0, 439.63, 442.26, 444.89, 447.52, 450.16, 452.79, 455.43, 458.06, 460.7, 463.34,
             465.98, 468.62, 471.26, 473.9, 476.54, 479.18, 481.83, 484.47, 487.12, 489.77, 492.42, 495.07, 497.72,
             500.37, 503.02, 505.67, 508.32, 510.98, 513.63, 516.29, 518.95, 521.61, 524.27, 526.93, 529.59, 532.25,
             534.91, 537.57, 540.24, 542.91, 545.57, 548.24, 550.91, 553.58, 556.25, 558.92, 561.59, 564.26, 566.94,
             569.61, 572.29, 574.96, 577.64, 580.32, 583.0, 585.68, 588.36, 591.04, 593.73, 596.41, 599.1, 601.78,
             604.47, 607.16, 609.85, 612.53, 615.23, 617.92, 620.61, 623.3, 626.0, 628.69, 631.39, 634.08, 636.78,
             639.48, 642.18, 644.88, 647.58, 650.29, 652.99, 655.69, 658.4, 661.1, 663.81, 666.52, 669.23, 671.94,
             674.65, 677.36, 680.07, 682.79, 685.5, 688.22, 690.93, 693.65, 696.37, 699.09, 701.81, 704.53, 707.25,
             709.97, 712.7, 715.42, 718.15, 720.87, 723.6, 726.33, 729.06, 731.79, 734.52, 737.25, 739.98, 742.72,
             745.45, 748.19, 750.93, 753.66, 756.4, 759.14, 761.88, 764.62, 767.36, 770.11, 772.85, 775.6, 778.34,
             781.09, 783.84, 786.58, 789.33, 792.08, 794.84, 797.59, 800.34, 803.1, 805.85, 808.61, 811.36, 814.12,
             816.88, 819.64, 822.4, 825.16, 827.92, 830.69, 833.45, 836.22, 838.98, 841.75, 844.52, 847.29, 850.06,
             852.83, 855.6, 858.37, 861.14, 863.92, 866.69, 869.47, 872.25, 875.03, 877.8, 880.58, 883.37, 886.15,
             888.93, 891.71, 894.5, 897.28, 900.07, 902.86, 905.64, 908.43, 911.22, 914.02, 916.81, 919.6, 922.39,
             925.19, 927.98, 930.78, 933.58, 936.38, 939.18, 941.98, 944.78, 947.58, 950.38, 953.19, 955.99, 958.8,
             961.6, 964.41, 967.22, 970.03, 972.84, 975.65, 978.46, 981.27, 984.09, 986.9, 989.72, 992.54, 995.35,
             998.17, 1000.99, 1003.81]

# the function below creates a list
# of the pixel values (equivalent to the brightness)
# of a hyperspectral image at coordinates (117, 42)
# (roughly the center of the image) across all
# 224 spectral bands


def brightness(img, bands):
    pixel_brightness = []
    pixel_value_x = 117
    pixel_value_y = 42
    for i in range(0, len(bands)):
        pixel_brightness.append(img[pixel_value_x, pixel_value_y, i])
    print('brightness levels of image are: ', pixel_brightness, '\n')
    return pixel_brightness

# the function below reads the wavelenths and adds them to a list


def wavelength(bands):
    pixel_wavelengths = []
    for i in range(0, len(bands)):
        pixel_wavelengths.append(bands[i])
    print('wavelengths of image are: ', pixel_wavelengths, '\n')
    return pixel_wavelengths


def day_list(image_day, bands):
    image_number = []
    for i in range(0, len(bands)):
        image_number.extend(image_day)
    print('image taken in day ', int(image_day))
    return image_number

# a plot comprised of 10 subplots
# each representing a day in the ripening process
# of an avocado
# the brightness of a specific pixel is recorded
# across all 224 bands and plotted in one subplot


def plot_spectral_signature(spectral_array):
    fig, axs = plt.subplots(2, 5, figsize=(10, 7))
    # axs.set_xlim(left=450, right=900)
    # axs.set_ylim(bottom=0, top=6)
    axs[0, 0].plot(spectral_array[0][0], spectral_array[0][1], 'tab:orange', linewidth=1)
    axs[0, 0].set_title('Image of day 1')
    axs[0, 0].set_ylim([0, 0.7])
    axs[0, 1].plot(spectral_array[1][0], spectral_array[1][1], 'tab:orange', linewidth=1)
    axs[0, 1].set_title('Image of day 2')
    axs[0, 1].set_ylim([0, 0.7])
    axs[0, 2].plot(spectral_array[2][0], spectral_array[2][1], 'tab:orange', linewidth=1)
    axs[0, 2].set_title('Image of day 3')
    axs[0, 2].set_ylim([0, 0.7])
    axs[0, 3].plot(spectral_array[3][0], spectral_array[3][1], 'tab:orange', linewidth=1)
    axs[0, 3].set_title('Image of day 4')
    axs[0, 3].set_ylim([0, 0.7])
    axs[0, 4].plot(spectral_array[4][0], spectral_array[4][1], 'tab:orange', linewidth=1)
    axs[0, 4].set_title('Image of day 5')
    axs[0, 4].set_ylim([0, 0.7])
    axs[1, 0].plot(spectral_array[5][0], spectral_array[5][1], 'tab:orange', linewidth=1)
    axs[1, 0].set_title('Image of day 6')
    axs[1, 0].set_ylim([0, 0.7])
    axs[1, 1].plot(spectral_array[6][0], spectral_array[6][1], 'tab:orange', linewidth=1)
    axs[1, 1].set_title('Image of day 7')
    axs[1, 1].set_ylim([0, 0.7])
    axs[1, 2].plot(spectral_array[7][0], spectral_array[7][1], 'tab:orange', linewidth=1)
    axs[1, 2].set_title('Image of day 8')
    axs[1, 2].set_ylim([0, 0.7])
    axs[1, 3].plot(spectral_array[8][0], spectral_array[8][1], 'tab:orange', linewidth=1)
    axs[1, 3].set_title('Image of day 9')
    axs[1, 3].set_ylim([0, 0.7])
    axs[1, 4].plot(spectral_array[9][0], spectral_array[9][1], 'tab:orange', linewidth=1)
    axs[1, 4].set_title('Image of day 10')
    axs[1, 4].set_ylim([0, 0.7])
    for ax in axs.flat:
        ax.set(xlabel='wavelengths', ylabel='brightness')
        ax.label_outer()
    fig.suptitle('Plot of spectral signature at pixel (117, 42) on 10 consecutive days', fontsize=16)
    plt.savefig("spectral_signature_plot_for_report.png")
    plt.show()

# these plots are a version of the plots in the
# function above, the difference being there are set
# boundaries for brightness values and number of bands
# for a better observation and interpretation of the plots
# each subplot (they are 10 in total), represents a day
# in which one avocado has been recorded in order to
# visualize the ripening process


def plot_spectral_signature_zoomed(spectral_array):
    fig, axs = plt.subplots(2, 5, figsize=(10, 7))
    axs[0, 0].plot(spectral_array[0][0], spectral_array[0][1], 'tab:orange', linewidth=1)
    axs[0, 0].set_title('Image of day 1')
    axs[0, 0].set_xlim([400, 450])
    axs[0, 0].set_ylim([0, 0.7])
    axs[0, 1].plot(spectral_array[1][0], spectral_array[1][1], 'tab:orange', linewidth=1)
    axs[0, 1].set_title('Image of day 2')
    axs[0, 1].set_xlim([400, 500])
    axs[0, 1].set_ylim([0, 0.7])
    axs[0, 2].plot(spectral_array[2][0], spectral_array[2][1], 'tab:orange', linewidth=1)
    axs[0, 2].set_title('Image of day 3')
    axs[0, 2].set_xlim([400, 500])
    axs[0, 2].set_ylim([0, 0.7])
    axs[0, 3].plot(spectral_array[3][0], spectral_array[3][1], 'tab:orange', linewidth=1)
    axs[0, 3].set_title('Image of day 4')
    axs[0, 3].set_xlim([400, 500])
    axs[0, 4].set_ylim([0, 0.7])
    axs[0, 4].plot(spectral_array[4][0], spectral_array[4][1], 'tab:orange', linewidth=1)
    axs[0, 4].set_title('Image of day 5')
    axs[0, 4].set_xlim([400, 500])
    axs[0, 4].set_ylim([0, 0.7])
    axs[1, 0].plot(spectral_array[5][0], spectral_array[5][1], 'tab:orange', linewidth=1)
    axs[1, 0].set_title('Image of day 6')
    axs[1, 0].set_xlim([400, 500])
    axs[1, 0].set_ylim([0, 0.7])
    axs[1, 1].plot(spectral_array[6][0], spectral_array[6][1], 'tab:orange', linewidth=1)
    axs[1, 1].set_title('Image of day 7')
    axs[1, 1].set_xlim([400, 500])
    axs[1, 1].set_ylim([0, 0.7])
    axs[1, 2].plot(spectral_array[7][0], spectral_array[7][1], 'tab:orange', linewidth=1)
    axs[1, 2].set_title('Image of day 8')
    axs[1, 2].set_xlim([400, 500])
    axs[1, 2].set_ylim([0, 0.7])
    axs[1, 3].plot(spectral_array[8][0], spectral_array[8][1], 'tab:orange', linewidth=1)
    axs[1, 3].set_title('Image of day 9')
    axs[1, 3].set_xlim([400, 500])
    axs[1, 3].set_ylim([0, 0.7])
    axs[1, 4].plot(spectral_array[9][0], spectral_array[9][1], 'tab:orange', linewidth=1)
    axs[1, 4].set_title('Image of day 10')
    axs[1, 4].set_xlim([400, 500])
    axs[1, 4].set_ylim([0, 0.7])
    for ax in axs.flat:
        ax.set(xlabel='wavelengths', ylabel='brightness')
        ax.label_outer()
    fig.suptitle('Plot of spectral signature at pixel (117, 42) on 10 consecutive days', fontsize=16)
    plt.savefig("spectral_signature_plot_xlabel_zoomed_for_report.png")
    plt.show()


# the same avocado is captured each day for 10 days
# here I read the front images and I compute the brightness
# at each wavelength
def import_vis_front():
    path = "E:\\hsi_dataset_files\\Avocado_version_2\\VIS_FRONT"
    fruit = "avocado_day_"
    fruit_number = "_01"
    front = "_front"
    bin_file = ".bin"
    hdr_file = ".hdr"
    png_file = ".png"
    complete_list = []
    for i in range(1, 11):
        if i == 10:
            day = str(i)
        else:
            day = "0" + str(i)
        file_name = path + "\\" + fruit + day + fruit_number + front
        rgb_file_name = fruit + day + fruit_number + front + png_file

        envi_FRONT = envi.open('%s%s' % (file_name, hdr_file),
                               '%s%s' % (file_name, bin_file))
        print('Image of day ', day)
        print(envi_FRONT, '\n')
        envi_data_NIR_FRONT = envi_FRONT.load()
        # print(envi_data_NIR_FRONT, '\n')
        header_FRONT = envi.read_envi_header('%s%s' % (file_name, hdr_file))
        print('ENVI header file:', '\n', header_FRONT, '\n')
        nested_list = [wavelength(VIS_BANDS), brightness(envi_FRONT, VIS_BANDS)]
        complete_list.append(nested_list)
        print("--------------------------------------------------------------------")
    # plot_spectral_signature(complete_list)
    plot_spectral_signature_zoomed(complete_list)


# import_vis_front()

# the same avocado is captured each day for 10 days
# here I read the back of the fruit images and I compute
# the brightness at each wavelength
def import_vis_back():
    path = "E:\\hsi_dataset_files\\Avocado_version_2\\VIS_BACK"
    fruit = "avocado_day_"
    fruit_number = "_01"
    back = "_back"
    bin_file = ".bin"
    hdr_file = ".hdr"
    png_file = ".png"
    complete_list = []
    for i in range(1, 11):
        if i == 10:
            day = str(i)
        else:
            day = "0" + str(i)
        file_name = path + "\\" + fruit + day + fruit_number + back
        rgb_file_name = fruit + day + fruit_number + back + png_file

        envi_BACK = envi.open('%s%s' % (file_name, hdr_file),
                              '%s%s' % (file_name, bin_file))
        print('Image of day ', day)
        print(envi_BACK, '\n')
        envi_data_NIR_FRONT = envi_BACK.load()
        # print(envi_data_NIR_FRONT, '\n')
        header_back = envi.read_envi_header('%s%s' % (file_name, hdr_file))
        print('ENVI header file:', '\n', header_back, '\n')
        nested_list = [wavelength(VIS_BANDS), brightness(envi_BACK, VIS_BANDS)]
        complete_list.append(nested_list)
        print("--------------------------------------------------------------------")
    plot_spectral_signature(complete_list)


#import_vis_back()

# The brightness of a pixel in three different images,
# each corresponding to one class "unripe", "ripe", "overripe"
# are plotted in order to observe clearer how the ripeness process
# influences it
def ripeness_check():
    img_day_1 = envi.open("avocado_day_01_20_front.hdr", "avocado_day_01_20_front.bin")
    img_day_5 = envi.open("avocado_day_05_14_front.hdr", "avocado_day_05_14_front.bin")
    img_day_10 = envi.open("avocado_day_10_01_front.hdr", "avocado_day_10_01_front.bin")
    spectral_day_1 = [VIS_BANDS, brightness(img_day_1, VIS_BANDS)]
    spectral_day_5 = [wavelength(VIS_BANDS), brightness(img_day_5, VIS_BANDS)]
    spectral_day_10 = [wavelength(VIS_BANDS), brightness(img_day_10, VIS_BANDS)]

    # ------spectral signature of 3 avocados in different ripeness stages -----
    plt.plot(spectral_day_1[0], spectral_day_1[1], '-b', label="unripe avocado")
    plt.plot(spectral_day_5[0], spectral_day_5[1], '-g', label="ripe avocado")
    plt.plot(spectral_day_10[0], spectral_day_10[1], '-r', label="overripe avocado")
    plt.title("Spectral Signature of 3 stages of ripeness")
    plt.xlabel("wavelengths")
    plt.ylabel("brightness")
    plt.legend(fontsize=8)
    plt.show()


ripeness_check()
