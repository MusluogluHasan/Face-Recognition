import cv2
import numpy as np

faceDetect=cv2.CascadeClassifier("haar/haarcascade_frontalface_default.xml") #Bu metot yüz bulma işlemini haarcascade sınıflandırıcısını kullanarak gerçekleştirir
cam=cv2.VideoCapture(1);

while(True):
	ret, img=cam.read();
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.3,5);

	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0) ,2)

	cv2.imshow("Face", img);
	if (cv2.waitKey(1) == ord('q')):
		break;

		cam.release()
		cv2.destroyAllwindows() 
