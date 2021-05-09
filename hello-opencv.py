import cv2

img = cv2.imread('images/lena.jpg', -1)
cv2.imshow("lena", img)
k = cv2.waitKey(0)

if k == ord('s'):
  cv2.imwrite('images/lena_copy.png', img)

cv2.destroyAllWindows()