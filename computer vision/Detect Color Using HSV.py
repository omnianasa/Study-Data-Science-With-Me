import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640 , 480)) #20 frsme 640 hight 480 width
def nothing(x):
    print(x)
cv2.namedWindow("TRACKING")

cv2.createTrackbar('LH', 'TRACKING', 0, 255, nothing)
cv2.createTrackbar('UH', 'TRACKING', 255, 255, nothing)
cv2.createTrackbar('LS', 'TRACKING', 0, 255, nothing)
cv2.createTrackbar('US', 'TRACKING', 255, 255, nothing)
cv2.createTrackbar('LV', 'TRACKING', 0, 255, nothing)
cv2.createTrackbar('UV', 'TRACKING', 255, 255, nothing)

print(cap.isOpened()) #check that the video is avilable

while(True):#we can write while(True)
    ret, frame = cap.read() #read evrything the camera sees #ret boolean variable if it has frames to be saved or not

    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    LH= cv2.getTrackbarPos('LH', 'TRACKING')
    UH = cv2.getTrackbarPos('UH', 'TRACKING')
    LV = cv2.getTrackbarPos('LV', 'TRACKING')
    UV = cv2.getTrackbarPos('UV', 'TRACKING')
    LS = cv2.getTrackbarPos('LS', 'TRACKING')
    US = cv2.getTrackbarPos('US', 'TRACKING')
    
    lowpar = np.array([LH, LS, LV])
    HIGHPAR = np.array([UH, US, UV])
    
    mask = cv2.inRange(hsv, lowpar, HIGHPAR)
    
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("frame", frame)        
    cv2.imshow("mask", mask)        
    cv2.imshow("res", res)  
    
    if cv2.waitKey(1) == ord('q'): #close the window
            break
        
  # have to write them to end every thing after finishing the program      
cap.release()
cv2.destroyAllWindows()