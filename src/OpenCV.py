import cv2
import numpy as np


FaceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default')
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('MyVid.avi', fourcc, 20.0, (640,480))
while True:
	ret, frame = cap.read()
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#out.write(frame)
	cv2.imshow('frames',frame)
	#faces = FaceDetect.detectMultiScale(frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()