import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)
while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_blur = cv.GaussianBlur(img,(7,7),0)
    edges = cv.Canny(img_blur,5, cv.CV_64F)
    filtered_img = cv.convertScaleAbs(edges)

    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.axis("off")

    plt.subplot(122),plt.imshow(edges,cmap='gray'),plt.title('Laplacian')
    plt.axis("off")
    plt.show()

    plt.draw()
    plt.pause(0.01)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    plt.show()

    cap.release
    cv.destroyAllWindows()