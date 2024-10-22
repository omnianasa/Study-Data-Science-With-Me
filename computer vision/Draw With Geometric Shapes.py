import cv2
import numpy as np
img = np.zeros((600, 900, 3), dtype = np.uint8)

#background
img = cv2.rectangle(img, (0,0) , (900,500) , (255,225,0), -1)
img = cv2.rectangle(img, (0,500) , (900,600) , (75,180,70), -1)

#sun
img = cv2.circle(img , (200, 150) , 60 , (0 , 225, 255), -1)
img = cv2.circle(img , (200, 150) , 65 , (255 , 255, 255), 3)

#Tree1
img = cv2.line(img , (710, 500) , (710, 420) , (30 , 65, 155), 25)
triangle = np.array([[640,460], [780,460], [710, 200]], np.int32)
img = cv2.fillPoly(img, [triangle], (75, 180, 70))

#Tree2
img = cv2.line(img , (600, 500) , (600, 420) , (30 , 65, 155), 25)
triangle = np.array([[500,440], [700,440], [600, 75]], np.int32)
img = cv2.fillPoly(img, [triangle], (75, 200, 70))

#text
font = cv2.FONT_HERSHEY_SIMPLEX 
img = cv2.putText(img, 'I love python', (10,300), font, 2, (0,255,255), 10)

cv2.imshow('Third image' , img)# reading the image to be shown
k = cv2.waitKey(0) # apply exit on the image
cv2.destroyAllWindows()