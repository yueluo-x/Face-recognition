import cv2


def Video():
    cap = cv2.VideoCapture(0)
    while (1):
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite(r'8.jpg', frame)
            break
    cap.release()
    #cv2.destroyAllWindows()
    cv2.destroyWindow("capture")
    return r'8.jpg'

