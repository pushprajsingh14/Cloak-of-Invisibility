import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # hsv lower: hue-10,100,100 higher: hue+10,255,255

        color = np.uint8([[[0, 0, 255]]])
        hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
        # print(hsv_black) to get hsv value

        lower = np.array([0, 100, 100])
        upper = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, lower, upper)

        behind_obj = cv2.bitwise_and(back, back, mask=mask)

        mask = cv2.bitwise_not(mask)

        part2 = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("magic", behind_obj + part2)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
