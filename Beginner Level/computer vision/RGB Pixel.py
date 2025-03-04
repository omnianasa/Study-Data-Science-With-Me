# Get RGB Of the pixel your mouse on
import cv2

def click_event(event, x, y, flags, param):
    global img, img_copy
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' , ', y)
        img = img_copy.copy()  # Reset to original image
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "x: " + str(x) + ' y: ' + str(y)
        img = cv2.putText(img, text, (x, y), font, 1, (0, 255, 255), 2)
        cv2.imshow('image', img)
    
    if event == cv2.EVENT_MOUSEMOVE:
        img = img_copy.copy() 
        red = img[y, x, 0]
        green = img[y, x, 1]
        blue = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"Red: {red} Green: {green} Blue: {blue}"
        img = cv2.putText(img, text, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow('image', img)

# Load image
img = cv2.imread('Pictures/img.jpg', 1)
img_copy = img.copy()  # Copy of original image for resetting

# Show image
cv2.imshow('image', img)

# Set mouse callback function
cv2.setMouseCallback('image', click_event)

# Wait until a key is pressed
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()

