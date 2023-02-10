import cv2
import numpy as np


def detectPlate(imgpath):
    faceCascade = cv2.CascadeClassifier('C:\\Users\pc\Desktop\\newgui\\newgui\\plateDetection\\haarcascade_russian_plate_number.xml')
    img = cv2.imread(imgpath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,
        minNeighbors = 5, minSize=(25,25))
    minArea = 50
    count=0
    for (x, y, w, h) in faces:
        area = w * h
        if area > minArea:
            # creating a rectangle around the plate number
            cv2.rectangle(img, (x, y), (x + w, y + h),(255,0,0),2)
            #  text over the detected plate nbr
            cv2.putText(img,"Plate number",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,128,223),2)
            #  to define our region of interest 
            img2=img[y:y+h,x:x+w]
            # display our region of interest
    
            cv2.imshow("PlateNbr",img2)

    cv2.imshow('plates',gray)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.imwrite("./plates/Image"+str(count)+".jpg",img2)
        count = count+1
        cv2.destroyAllWindows()
