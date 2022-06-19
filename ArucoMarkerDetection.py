
import cv2
import numpy as np

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
arucoParams = cv2.aruco.DetectorParameters_create()

#webcam height and width
wCam, hCam = 1280, 720

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0

while True:
    success, img = cap.read()
    (corners, _, _) = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)
    int_corners = np.int0(corners)

    if corners:
        cv2.polylines(img, int_corners, True, (0,255,0),2)
        arucoPerimeter = cv2.arcLength(corners[0], True)

        #pixel to cm ratio
        pixel_cm_ratio = arucoPerimeter/20  # 20 cm is the actual perim of the object

    cv2.imshow("Image", img)
    cv2.waitKey(1)
