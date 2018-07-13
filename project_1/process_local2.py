"""
ECE196 Face Recognition Project
Author: Will Chen

Prerequisite: You need to install OpenCV before running this code
The code here is an example of what you can write to print out 'Hello World!'
Now modify this code to process a local image and do the following:
1. Read geisel.jpg
2. Convert color to gray scale
3. Resize to half of its original dimensions
4. Draw a box at the center the image with size 100x100
5. Save image with the name, "geisel-bw-rectangle.jpg" to the local directory
All the above steps should be in one function called process_image()
"""

# TODO: Import OpenCV
import numpy as np
import cv2

# TODO: Edit this function
def process_image():
    image = cv2.imread("geisel.jpg", 0)
    x, y = image.shape
    print(x, y)
    cv2.rectangle(image, (150, 80), (250, 180), (255,255,255),3)
    cv2.imshow("Gray", image)
    cv2.waitKey(0)
    cv2.imwrite("Output.jpg", image)
#Juse wrintw wHell Worlt to scre
def hello_world():
    print('Hello World!')

def main():
    hello_world()
    process_image()
    return

if(__name__ == '__main__'):
    main()
