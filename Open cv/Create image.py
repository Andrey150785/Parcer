import cv2
import numpy as np

photo = np.zeros((500, 500, 3), dtype='uint8')
# photo[300:450, 200:280] = 80, 35, 189

# cv2.rectangle(photo, (50, 70), (100, 100), (119, 201, 105), thickness=1)
# cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1]//3, photo.shape[0] // 2), (56, 200, 115), thickness=5)
cv2.putText(photo, 'itProger', (100, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness=1)
# cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 50, (119, 201, 105), thickness=cv2.FILLED)
cv2.imshow('Photo', photo)
cv2.waitKey(0)