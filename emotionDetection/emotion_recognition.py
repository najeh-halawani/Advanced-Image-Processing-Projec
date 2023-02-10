import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

def image_emotion(imgPath):
    img = cv2.imread(imgPath)
    # cv2.imshow('colored image', img)
    # cv2.waitKey(0)

    plt.imshow(img[:, :, : : -1])
    plt.show()
    predictions = DeepFace.analyze(img, actions = ['emotion'])

    print(predictions)
    # type(predictions) -> dict -> predictions['dominant_emotion']

    # trying to draw a rectangle across the face
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.1,4)

    # Draw a rectangle around the face
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(img, predictions['dominant_emotion'],(250,250),font,5,(0,0,255), cv2.LINE_4)
    plt.imshow(img[:, :, : : -1])
    plt.show()