import numpy as np
import cv2

img = np.zeros([512, 512, 3], np.uint8)
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)
img = cv2.rectangle(img, (0, 0), (255, 255), (255, 0, 0), 5)
img = cv2.circle(img, (55, 55), 55, (0, 255, 0), 5)
img = cv2.putText(img, 'OpenCV', (255, 255), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 5, cv2.LINE_AA)

cv2.imshow("lena", img)
cv2.waitKey(0)
cv2.destroyAllWindows()