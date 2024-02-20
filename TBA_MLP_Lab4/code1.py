import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('C:\\Users\\Gio Vincent\\Documents\\ADU FILES\\MLP_Lab\\MPL_Lab-main\\TBA_MLP_Lab4\\Images\\Cody.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_blur = cv.GaussianBlur(img,(7,7),0)

sobelx = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
filtered_image_x = cv.convertScaleAbs(sobelx)
sobely = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
filtered_image_y = cv.convertScaleAbs(sobely)
sobelxy = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
filtered_image_xy = cv.convertScaleAbs(sobelxy)

plt.figure(figsize=(20,20))

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.axis("off")

plt.subplot(222),plt.imshow(filtered_image_x, cmap = "gray"),plt.title('Filtered Image x-axis')
plt.axis("off")

plt.subplot(223),plt.imshow(filtered_image_y, cmap = "gray"),plt.title('Filtered Image y-axis')
plt.axis("off")

plt.subplot(224),plt.imshow(filtered_image_xy, cmap = "gray"),plt.title('Filtered Image xy-axis')
plt.axis("off")

plt.show()