import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640 , 480)) #20 frsme 640 hight 480 width
while(True):#we can write while(True)
    ret, frame = cap.read() #read evrything the camera sees #ret boolean variable if it has frames to be saved or not

    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    cx = int(width/2)
    cy = int(height/2)
    hue = hsv[cy, cx][0]
    color = 'nan'
    if hue <5:
        color = 'red'
    elif hue <22:
        color = 'orange'
    elif hue <33:
        color = 'yellow'
    elif hue <78:
        color = 'green'
    elif hue <131:
        color = 'blue'
    elif hue <170:
        color = 'violet'
    else:
        color = 'red'
    pixel_bgr = frame[cy, cx]
    
    b, g, r = int(pixel_bgr[0]), int(pixel_bgr[1]), int(pixel_bgr[2])

    
    cv2.putText(frame, color, (cx-50, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    cv2.imshow("Frame", frame)
    #out.write(frame) #save your video     
    
    if cv2.waitKey(1) == ord('q'): #close the window
            break
        
  # have to write them to end every thing after finishing the program      
cap.release()
cv2.destroyAllWindows()

