import cv2 as cv
from matplotlib import pyplot as plt

font = cv.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (0, 0, 0)
thickness = 4

img = cv.imread('C:\\Users\\Gio Vincent\\Documents\\ADU FILES\\MLP_Lab\\MPL_Lab-main\\TBA_MLP_Lab3\\Images\\Blue.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

avg = cv.blur(img,(10,10))
gau = cv.GaussianBlur(img,(7,7),0)
med = cv.medianBlur(img,5)
bil = cv.bilateralFilter(img,9,75,75)

original = cv.putText(img,'Original', org,font,fontScale,color,thickness)
average = cv.putText(avg,'Average', org,font,fontScale,color,thickness)
gaussian = cv.putText(gau,'Gaussian', org,font,fontScale,color,thickness)
median = cv.putText(med,'Median', org,font,fontScale,color,thickness)
bilateral = cv.putText(bil,'Bilateral Filtering', org,font,fontScale,color,thickness)

plt.subplot(3,3,5),plt.imshow(original),plt.title('Original')
plt.xticks([]),plt.yticks([])

plt.subplot(3,3,1),plt.imshow(avg),plt.title('Average')
plt.xticks([]),plt.yticks([])

plt.subplot(3,3,3),plt.imshow(gau),plt.title('Gaussian Blur')
plt.xticks([]),plt.yticks([])

plt.subplot(3,3,7),plt.imshow(med),plt.title('Median Blur')
plt.xticks([]),plt.yticks([])

plt.subplot(3,3,9),plt.imshow(bil),plt.title('Bilateral Filtering')
plt.xticks([]),plt.yticks([])
plt.show()