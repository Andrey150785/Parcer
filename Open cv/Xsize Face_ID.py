import cv2
import numpy as np

img = cv2.imread("book3.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
results = faces.detectMultiScale(img, scaleFactor=2, minNeighbors=1)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=1)

cv2.imshow("Result", img)

cv2.waitKey(0)