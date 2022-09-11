from unittest import result
import cv2
import mediapipe as mp
import time
camera=cv2.VideoCapture(0)  
mpmana=mp.solutions.hands 
mana=mpmana.Hands()
mpdesen=mp.solutions.drawing_utils
 
while True:
 
    succes,imagine=camera.read()
    convertRGB=cv2.cvtColor(imagine,cv2.COLOR_BGR2RGB)  
    rezultat=mana.process(convertRGB) 
    if rezultat.multi_hand_landmarks: 
        for manalms in rezultat.multi_hand_landmarks:  
              for id,lm in enumerate(manalms.landmark):
                
                h, w,c = imagine.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                font = cv2.FONT_HERSHEY_SIMPLEX
                a=id
                a=str(a)
                cv2.rectangle(imagine, (cx, cy),(cx+25, cy+30), (50,205,50  ),  15)
                cv2.putText(imagine,a,(cx,cy), font, 0.5,(0,0,0),2,cv2.LINE_AA)
       
                mpdesen.draw_landmarks(imagine,manalms,mpmana.HAND_CONNECTIONS) 

   
    cv2.imshow("Camera",imagine)  
    cv2.waitKey(1)