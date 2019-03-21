import numpy as np
import cv2

cap = cv2.VideoCapture('Perfect Blue.mp4')
arr = []

ret, frame = cap.read()

while(ret != 0):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    avg = np.average(gray)
    arr.append(avg)

    ret, frame = cap.read()


print(arr)
np.savetxt('perfect.txt', arr, fmt='%3.3f', delimiter=',')

cap.release()
cv2.destroyAllWindows()
