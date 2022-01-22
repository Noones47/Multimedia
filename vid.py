from PIL import Image
import cv2
import os
import glob
import numpy
import shutil
import re


def save_frames():
    vidcap = cv2.VideoCapture('video1.mp4')
    success, image = vidcap.read()
    count = 1
    while success:
        cv2.imwrite("%dframe.jpg" % count, image)  # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1

    dst_folder = 'C:/PythonProjects/frames'
    pattern = '*frame.jpg'
    files = glob.glob(pattern, recursive=False)
    for file in files:
        # extract file name form file path
        # file_name = os.path.basename(file)
        shutil.move(file, dst_folder)
        print('Moved:', file)


def bw():
    img_dir = "C:/PythonProjects/frames"  # Directory of all images
    data_path = os.path.join(img_dir, '*frame.jpg')  # Filter becouse I only want some type of images
    files = glob.glob(data_path)
    data = []

    plus = Image.open(
        "C:/PythonProjects/frames/12frame.jpg")  # getting the image just to get his size for the FOR cycle

    for j in files:
        img = cv2.imread(j)
        data.append(img)  # Save the images into a list
    count = 1
    for i in range(0, 73):  # 128 are the numbers of images I want to work with
        img_data = data[i]  # Select image by image from the list

        # Run the image
        lst = []
        for x in img_data:
            for y in x:
                lst.append(y[0] * 0.2125 + y[1] * 0.7169 + y[2] * 0.0689)  # Using the pixels then saving them to a List
        # New Image
        new_image = Image.new("L", plus.size)
        new_image.putdata(lst)  # Put the data from the list to the new image

        new_image = numpy.array(new_image)
        # Save the image
        cv2.imwrite("%dbwframe.jpg" % count, new_image)
        count += 1

    dst_folder = 'C:/PythonProjects/bwframes'
    pattern = '*bwframe.jpg'
    files = glob.glob(pattern, recursive=False)
    for file in files:
        # extract file name form file path
        # file_name = os.path.basename(file)
        shutil.move(file, dst_folder)
        print('Moved:', file)

    destination2 = 'C:/PythonProjects/trash'
    files_to_move = ['C:/PythonProjects/bwframes/11bwframe.jpg', 'C:/PythonProjects/bwframes/22bwframe.jpg',
                     'C:/PythonProjects/bwframes/33bwframe.jpg',
                     'C:/PythonProjects/bwframes/44bwframe.jpg', 'C:/PythonProjects/bwframes/55bwframe.jpg',
                     'C:/PythonProjects/bwframes/66bwframe.jpg']
    # iterate files
    for file in files_to_move:
        # move file
        shutil.move(file, destination2)
        print('Moved:', file)


def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [
        int(text)
        if text.isdigit() else text.lower()
        for text in _nsre.split(s)]


def makevid():
    image_folder = 'C:/PythonProjects/bwframes'
    video_name = 'videofinal.avi'

    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 20, (width, height))

    sorted_images = sorted(images, key=natural_sort_key)

    for image in sorted_images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

def mainvid():
    save_frames()
    bw()
    makevid()
