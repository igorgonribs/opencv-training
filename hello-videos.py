import cv2
import datetime

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()
  if ret == True:
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    text = str(datetime.datetime.now())
    cv2.putText(frame, text, (10, 50), fonte, 1, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  
  else:
    break

cap.release()
cv2.destroyAllWindows()