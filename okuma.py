import cv2
import numpy as np
from PIL import Image
import pickle
import sqlite3

faceDetect=cv2.CascadeClassifier("haar/haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(0);

rec=cv2.face.LBPHFaceRecognizer_create();
rec.read("recognizer/trainningData.yml")

def getProfile(id):
	conn=sqlite3.connect("face_database.db")
	cmd="SELECT * FROM People WHERE ID ="+str(id)
	cursor=conn.execute(cmd)
	profile=None
	for row in cursor:
		profile=row
	conn.close()
	return profile 
#id=0
font=cv2.FONT_HERSHEY_SIMPLEX #kameradan okutulan kişinin bilgilerinin yazıldığı ifade.
fontColor= (194,244,66)
fontScale= 1
while(True):
	ret, img=cam.read();
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.3,5);

	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y),(x+w,y+h),(244,229,66) ,2)
		id, conf=rec.predict(gray[y:y+h, x:x+w])
		
		profile=getProfile(id)
		if (profile!=None):   
			cv2.putText(img,str(profile[1]),(x,y+h+30),font,fontScale, fontColor);
	cv2.imshow("Face", img);
	if (cv2.waitKey(1) == ord('q')):
		break;
		cam.release()
		cv2.destroyAllwindows() 
