import cv2
import numpy as np
import matplotlib.image as img
import os

from PIL import Image


def resize():
    img = cv2.imread('img2.jpg')

    # print shape of the image
    # using shape attribute
    print("Tamanho original:", img.shape)

    # assigning number of rows, coulmns and
    # planes to the respective variables
    row, col, plane = img.shape

    # the value by which we want to resize the image
    # here we want to resize an image as one half of the original image
    x, y = 2, 2

    # assign red of the RGB image

    blue_plane = img[:, :, 0]
    # assign green of the RGB image
    green_plane = img[:, :, 1]

    # assign blue of the RGB image
    red_plane = img[:, :, 2]

    # we take one-half pixel of rows and columns from
    # each plane respectively so that, it is one-half of image matrix.

    resize_blue_plane = blue_plane[1::x, 1::x]

    resize_green_plane = green_plane[1::x, 1::x]

    resize_red_plane = red_plane[1::x, 1::x]

    # create a zero matrix of specified order of 3-dimension
    resize_img = np.zeros((row // x, col // y, plane), np.uint8)

    # assigning resized blue, green and red plane of image matrix to the
    # corresponding blue, green, red plane of resize_img matrix variable.
    resize_img[:, :, 0] = resize_blue_plane
    resize_img[:, :, 1] = resize_green_plane
    resize_img[:, :, 2] = resize_red_plane

    cv2.imwrite('resize.jpg', resize_img)

    print("resize image shape:", resize_img.shape)

    img2 = cv2.imread('resize.jpg')

    taxa = img2.size / img.size

    print("Taxa de compressao é", img2.size, "/", img.size, "=", taxa)


def cropping():
    # reading image in variable m
    m = img.imread("img4.png")

    # determining dimension of image width(w) height(h)
    w, h = m.shape[:2]

    # required image size after cropping
    xNew = int(w * 1 / 3)
    yNew = int(h * 1 / 3)
    newImage = np.zeros([xNew, yNew, 4])

    # print width height of original image
    print("widht:", w)
    print("height:", h)

    for i in range(1, xNew):
        for j in range(1, yNew):
            # cropping start from 50, 50 pixel of original image(this can be changed)
            newImage[i, j] = m[50 + i, 50 + j]

    # save image
    img.imsave('cropped.png', newImage)

    img2 = cv2.imread('cropped.png')
    taxa = img2.size / m.size
    print("Taxa de compressao é", img2.size, "/", m.size, "=", taxa)


def compressMe(file):
    # Get the path of the file
    filepath = 'C:/PythonProjects/frames'

    # open the image
    picture = Image.open('img1.jpg')
    picture.save("Compressed_" + file,
                 "JPEG",
                 optimize=True,
                 quality=10)
    return


# Define a main function
def multicompress():
    # finds current working dir
    cwd = os.getcwd()

    formats = ('.jpg', '.jpeg')

    for file in os.listdir(cwd):

        # If the file format is JPG or JPEG
        if os.path.splitext(file)[1].lower() in formats:
            print('compressing', file)
            compressMe(file)

    print("Done")



