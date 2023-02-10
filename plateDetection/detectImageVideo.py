import cv2
import numpy as np

frameWidth = 640    #Frame Width
frameHeight = 480   # Frame Height

# code to access a file from the lib cv2 that will let
# us detect nbr plate of vehicles

# this .xml file is the pretrained file/model
# for detecting the number of the plate



# code to open the camera
def PlateDetection():
    plateCascade = cv2.CascadeClassifier("C:\\Users\pc\Desktop\\newgui\\newgui\\plateDetection\\haarcascade_russian_plate_number.xml")
    minArea = 500
    cap =cv2.VideoCapture(0)
    cap.set(3,frameWidth)
    cap.set(4,frameHeight)
    cap.set(10,150)
    count = 0
    while True:
        success, img = cap.read()
        # img = cv2.flip(img, 1)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)
        for (x, y, w, h) in numberPlates:
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
        cv2.imshow("Camera", img)
        # code to take a ss of the plate nb and save it
    
        # pressing s on your keyboard will save the detected nbr plate
        if cv2.waitKey(1) & 0xFF == ord('s'):
            # defining where our ss will be saved
            cv2.imwrite("./plates/Image"+str(count)+".jpg",img2)
            cv2.rectangle(img,(0,200),(640,400),(0,0,255),cv2.FILLED)
            # after pressing they keyCap s 
            # Scan saved will be displayed on the screen
            cv2.putText(img,"Scan Saved",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2)
            cv2.imshow("Result",img)
            cv2.waitKey(10)
            count=count+1
            break

# PlateDetection()
        
        
        
  

