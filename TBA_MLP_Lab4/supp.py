import cv2 as cv
from matplotlib import pyplot as plt
cap = cv.VideoCapture(0)
while True:
    ret, img = cap.read()
    if not ret:
        break
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_blur = cv.GaussianBlur(img_gray,(7,7),0)

    sobelx = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
    filtered_image_x = cv.convertScaleAbs(sobelx)
    sobely = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
    filtered_image_y = cv.convertScaleAbs(sobely)
    sobelxy = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
    filtered_image_xy = cv.convertScaleAbs(sobelxy)
    canny = cv.Canny(img_gray, 100, 200)
    filtered_canny = cv.convertScaleAbs(canny)
    laplace = cv.Canny(img_blur, 5, cv.CV_64F)
    filtered_img = cv.convertScaleAbs(laplace)

    plt.figure(figsize=(20, 20))
    plt.subplot(231), plt.imshow(img), plt.title('Original')
    plt.axis("off")
    plt.subplot(232), plt.imshow(filtered_image_x, cmap="gray"), plt.title('Filtered Image x-axis')
    plt.axis("off")
    plt.subplot(233), plt.imshow(filtered_image_y, cmap="gray"), plt.title('Filtered Image y-axis')
    plt.axis("off")
    plt.subplot(234), plt.imshow(filtered_image_xy, cmap="gray"), plt.title('Filtered Image xy-axis')
    plt.axis("off")
    plt.subplot(235), plt.imshow(canny, cmap='gray'), plt.title('Canny')
    plt.axis("off")
    plt.subplot(236), plt.imshow(laplace, cmap='gray'), plt.title('Laplacian')
    plt.axis("off")
    plt.draw()
    plt.pause(0.01)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    plt.show()
    cap.release
    cv.destroyAllWindows()