# import cv2, numpy and matplotlib libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\STUDENT\\PycharmProjects\\TBA_SDL_Lab1\\Images\\Flower.jpg")
# Displaying image using plt.imshow() method
plt.imshow(img)

# hold the window
plt.waitforbuttonpress()
plt.close('all')