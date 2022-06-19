# Script which calls HandTrackingModule and ...
# 1) plots line connecting the index and thumb
# 2) calculates the precision grip aperture and prints it

import cv2
import time
import HandTrackingModule as htm
import math
import numpy as np

# loading details of the aruco marker we are using
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
arucoParams = cv2.aruco.DetectorParameters_create()

#webcam height and width
wCam, hCam = 1280, 720

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0
detector = htm.HandDetector(detectionConfidence=0.7)

while True:
    success, img = cap.read()
    (corners, _, _) = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)
    int_corners = np.int0(corners)
    if corners:
        img = detector.findHands(img)
        # find the aruco marker in video
        cv2.polylines(img, int_corners, True, (0,255,0),2)
        arucoPerimeter = cv2.arcLength(corners[0], True)
        # calculate pixel to cm ratio
        pixel_cm_ratio = arucoPerimeter/20  # 20 cm is the actual perim of the object

        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:  # if a hand is visible ...
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]

            cx, cy = (x1+x2)//2, (y1+y2)//2  # getting the center of the line

            cv2.circle(img, (x1,y1), 10,(255,255,255))
            cv2.circle(img, (x2,y2), 10,(255,255,255))
            cv2.line(img,(x1,y1), (x2,y2),(0,0,255),1)  # draw line connecting the 2 fingers
            cv2.circle(img, (cx,cy),2,(255,255,255),cv2.FILLED)

            distance = math.hypot(x2-x1,y2-y1)  # distance between index and thumb (distance in pixels)
            distance = distance/pixel_cm_ratio
            print(distance)  # distance between index and thumb in cm

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.imshow("Image", img)
    cv2.waitKey(1)

