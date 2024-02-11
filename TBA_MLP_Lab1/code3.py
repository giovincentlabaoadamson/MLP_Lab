
import cv2

# path
path = "C:\\Users\\STUDENT\\PycharmProjects\\TBA_SDL_Lab1\\Images\\Flower.jpg"

# Using cv2.imread() method
# Using 0 to read image in grayscale mode
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Displaying the image
cv2.imshow('image', img)
cv2.waitKey(7000)
cv2.destroyAllWindows()