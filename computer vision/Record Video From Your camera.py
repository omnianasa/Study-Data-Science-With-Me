# Record A video from your webcam

import cv2
import datetime
print(cv2.__version__)

# Asecond programme to make a video in grey of yourself using the lap camera
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640 , 480)) #20 frsme 640 hight 480 width

#old width and height
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#make new width and height
cap.set(3,3000) #3for width 4for height
cap.set(4,3000)

#get the new values
print(cap.get(3))
print(cap.get(4))

print(cap.isOpened()) #check that the video is avilable
while(True):#we can write while(True)
    ret, frame = cap.read() #read evrything the camera sees #ret boolean variable if it has frames to be saved or not
    
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #print the width and height of the video
        out.write(frame) #write all frames in the video specified
        
        #add date and time to the video
        font = cv2.FONT_HERSHEY_SIMPLEX #make the fint face
        text = "Width "+ str(cap.get(3)) + "   Height " + str(cap.get(4)) #the text of the width and height of the video
        date = str(datetime.datetime.now()) #the text of the date and time of the real time state
        frame = cv2.putText(frame, text, (10,50), font, 1, (0,0,0), 2) #draw the first line of dimensions
        frame = cv2.putText(frame, date, (10,100), font, 1, (0,0,0), 2) #draw the second line of the date
        
        # turn RGB to grey
        #gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        
        cv2.imshow('frame' , frame)
        
        if cv2.waitKey(1) == ord('q'): #close the window
            break
    else:
        break
        
  # have to write them to end every thing after finishing the program      
cap.release()
out.release()
cv2.destroyAllWindows()
