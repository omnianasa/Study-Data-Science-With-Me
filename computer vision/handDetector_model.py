

import cv2
import mediapipe as mlp
import time

class HandTracking():
    def __init__(self):
        #self.mode = mode
        
        self.mphands = mlp.solutions.hands
        #static_image_mode is false cause it doesnot detect everytime with left and right hands
        self.hands = self.mphands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) 
        self.mpdraw = mlp.solutions.drawing_utils # make connection between points



    def findHands(self, img, draw = True):
            RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.output = self.hands.process(RGB) #mediapipe works with RGB frames
            if self.output.multi_hand_landmarks:
                for i in self.output.multi_hand_landmarks:
                    if draw:
                        self.mpdraw.draw_landmarks(img, i, self.mphands.HAND_CONNECTIONS) #check if there is a landmark and draw it WITH connections between them
            return img

    def findPosition(self, img, handnum = 0, draw = True):
         lmlist = []
         if self.output.multi_hand_landmarks:
              hand = self.output.multi_hand_landmarks[handnum]
              for index, lm in enumerate(hand.landmark):
                   h, w, c = img.shape
                   cx, cy = int(lm.x * w), int(lm.y * h)
                   lmlist.append([index, cx, cy])
                   #if draw:
                    #    cv2.circle(img, (cx, cy), 5, (0,0,0), cv2.FILLED)
         return lmlist

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1285)
    cap.set(4, 758)
    # detect the landmarks of hand marks
    model = HandTracking()
    while True:
        _, frame = cap.read()
       
        frame = model.findHands(frame)
        lista = model.findPosition(frame)
        if len(lista)!=0:
             print(lista[4])
        #count the frame per second
        previous_time = 0
        current_time = 0
        current_time = time.time()
        fps = 1/(current_time - previous_time)
        previous_time = current_time

        cv2.putText(frame, f"FPS: {int(fps)}", (15, 60), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 0)) #write the text of frames per second
        cv2.imshow("frame", frame)#show the frame 
        if cv2.waitKey(1) == ord('q'): #close the window
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

    

