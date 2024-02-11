import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# loop runs if capturing has been initialized.
while cap.isOpened():

    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting....")
        break
    # The window showing the operated video stream
    cv.imshow('original', frame)

    # Converts to HSV color space, OCV reads colors as BGR
    # frame is converted to hsv
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # output the frame
    out.write(hsv)
    cv.imshow('frame', hsv)
    # Wait for 'q' key to stop the program
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()