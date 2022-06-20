# HandTracking

Repository Contents:

1. HandTrackingModule.py: this is the main module that uses openCV and Google's mediapipe hands library to display the hand in real time. 
2. BasicHandTracker.py: sample script that calls the HandTrackingModule. 
3. ArucoMarkerDetection.py: sample script that finds the Aruco marker in this repository and highlights it. 
4. Aruco Marker.jpg: DICT_5X5_50 Aruco marker. You will need to print this and have it visible to the camera. Size of the marker should remain at 5x5 cm.
5. PrecisionGripAperture.py: Script that waits for arcuo marker to be visible in camera, then calls HandTrackingModule, and calcualtes the grip aperture (index to thumb) and prints it in cm. By using the aruco marker, we can convert distance in pixels to cm while taking depth into account. 
