import cv2
# define a video capture object
vid = cv2.VideoCapture(0)
while(True):
    # Capture the video frame
    ret, frame = vid.read()
    # Display the resulting frame
    cv2.imshow('frame', frame)

    # the 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()