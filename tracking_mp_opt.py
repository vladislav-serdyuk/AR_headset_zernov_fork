import mediapipe as mp
import cv2
import numpy as np
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from math import dist

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

segmentor = SelfiSegmentation()
class controller():
    
    def remove_background(self,img,minx,miny,maxx,maxy):
        try:
            img = img[miny:maxy, minx:maxx]
            gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
            _, mask = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 
            mask = cv2.bitwise_not(mask)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))

            result = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
            result[:, :, 3] = mask

            return result
        except:
            return img
            pass
    
    def find_and_get_hands(self, image):
        results = hands.process(image)

        lmList = []
        miny, minx, maxy, maxx = 0, 0, 0, 0

        if results.multi_hand_landmarks:
            myHand = results.multi_hand_landmarks[0]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

        if len(lmList) >= 20:
            lmArray = np.array(lmList)
            xlist = lmArray[:, 1]
            ylist = lmArray[:, 2]
            distance = (1500-dist(*[(np.clip(np.min(xlist) - 30, 1, None), np.clip(np.min(ylist) - 30, 1, None)), (np.clip(np.max(xlist) + 30, 1, None), np.clip(np.max(ylist) + 30, 1, None))]))//10
            if (distance < 115 and distance > 0):
                return lmList, miny, minx, maxy, maxx, distance
            else:
                return [],0,0,0,0,0
        else:
            return lmList, miny, minx, maxy, maxx, 0

