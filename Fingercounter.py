import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

wCam , hCam = 640 , 480

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

detector = htm.HandDetector(detectionCon=0.75)


while True:
    success , img = cap.read()
    img = detector.findHands(img)
    lmList = detector.FindPosition(img,draw=True)
    # print(lmList)    
    
    tipsIds = [4,8,12,16,20]
    
    if len(lmList) != 0:
        if(lmList[5][1] > lmList[9][1]):
        
            if(len(lmList)!= 0 ):
                fingers = []
    
                if lmList[4][1] > lmList[3][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
    
                for i in range(1,5):
                    if lmList[tipsIds[i]][2] < lmList[tipsIds[i]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
    
    
                print(fingers)
    
                cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
                cv2.putText(img, str(fingers.count(1)), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), thickness=5)
    
    
            # if(len(lmList)!= 0 ):
            #     if lmList[8][2] < lmList[6][2]:
            #         print("Index Finger Open")
    
         
        else:
        
            if(len(lmList)!= 0 ):
                fingers = []
    
                if lmList[4][1] < lmList[3][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
    
                for i in range(1,5):
                    if lmList[tipsIds[i]][2] < lmList[tipsIds[i]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
    
    
                print(fingers)
    
                cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
                cv2.putText(img, str(fingers.count(1)), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), thickness=5)
    
    
            # if(len(lmList)!= 0 ):
            #     if lmList[8][2] < lmList[6][2]:
            #         print("Index Finger Open")
    
    

    
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    cv2.putText(img,f'FPS : {int(fps)}',(10,40), cv2.FONT_HERSHEY_COMPLEX,1.3 , (255,0,0),3)
    
    
    cv2.imshow("Image" , img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break