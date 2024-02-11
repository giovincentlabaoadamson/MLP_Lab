import cv2

img = cv2.imread("C:\\Users\\Gio Vincent\\Documents\\ADU FILES\\MLP_Lab\\MPL_Lab-main\\TBA_MPL_Lab1\\Images\\Flower.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Flower", img)
cv2.waitKey(0)
cv2.destroyAllWindows()