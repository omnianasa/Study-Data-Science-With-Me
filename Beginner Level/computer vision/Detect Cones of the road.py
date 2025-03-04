import cv2
import numpy as np

y_counter = 0
b_counter = 0

cap = cv2.VideoCapture('Videos/Car.mp4')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('carcairo.avi', fourcc, 30, (1280, 720))

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while (ret):
    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    
    
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])
    
    y_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    b_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    
    kernel = np.ones((5, 5), np.uint8)
    yellow_mask = cv2.morphologyEx(y_mask, cv2.MORPH_CLOSE, kernel)
    blue_mask = cv2.morphologyEx(b_mask, cv2.MORPH_CLOSE, kernel)
    
    y_contours, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    b_contours, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    
    for i in y_contours:
            (x, y, w, h) = cv2.boundingRect(i)
            if x > 1000:
                cv2.rectangle(frame1, (x, y), (x + w + 2, y + h + 2), (0, 255, 255), 3)
            
    for i in b_contours:
            (x, y, w, h) = cv2.boundingRect(i)
            if x < 600:
                cv2.rectangle(frame1, (x, y), (x + w + 2, y + h + 2), (255, 255, 0), 3)
       
    image = cv2.resize(frame1, (1280, 720))
    out.write(image)
    cv2.imshow("motion detection", frame1)
    frame1 =frame2
    ret, frame2 = cap.read()
    if cv2.waitKey(1) == ord('q'): #close the window
        break
    
cv2.destroyAllWindows()
cap.release()
out.release()
