#sample script that calls the HandTrackingModule

import cv2
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0) # chose the webcam number
detector = htm.HandDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # display FPS data on video
    cv2.putText(img, 'FPS', (10,35), cv2.FONT_HERSHEY_DUPLEX,1, (255,255,255),2)
    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_DUPLEX,1, (255,255,255),2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
