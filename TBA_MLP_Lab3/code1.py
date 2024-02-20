import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('C:\\Users\\Gio Vincent\\Documents\\ADU FILES\\MLP_Lab\\MPL_Lab-main\\TBA_MLP_Lab3\\Images\\Blue.jpg')

blur = cv.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]),plt.yticks([])
plt.show()