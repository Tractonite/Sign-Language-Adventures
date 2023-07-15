import pyautogui
import time
import mediapipe as mp
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math


def handDetect():
  counter = 0
  folder = "Data/B"
  cap = cv2.VideoCapture(0)
  detector = HandDetector(maxHands=2)
  classifier = Classifier("Model/keras_model.h5","Model/labels.txt")
  offset = 20
  imgSize = 300
  labels = ["A","B"]
  # a new comment
  try:
    while True:
      success, img = cap.read()
      hands,img = detector.findHands(img)
      if hands:
        if len(hands) == 2:
          hand1 = hands[0]
          hand2 = hands[1]
          try:
    # Get the bounding boxes for both handsB
            x1, y1, w1, h1 = hand1['bbox']
            x2, y2, w2, h2 = hand2['bbox']
            x_combined = min(x1, x2)
            y_combined = min(y1, y2)
            w_combined = max(x1 + w1, x2 + w2) - x_combined
            h_combined = max(y1 + h1, y2 + h2) - y_combined
            imgCombined = img[y_combined - offset:y_combined + h_combined+offset, x_combined - offset:x_combined + w_combined+ offset]
            imgCombined = cv2.resize(imgCombined, (imgSize, imgSize))
            cv2.imshow("Image", imgCombined)
            time.sleep(0.1)
            prediction,index = classifier.getPrediction(imgCombined)
            print(prediction,labels[index])
            
            if labels[index] == 'A':
              print("A pressed")
              pyautogui.keyDown('A')
              time.sleep(0.4)
              pyautogui.keyUp('A')
            elif labels[index] == 'B':
              print("B Pressed")
              pyautogui.keyDown('B')
              time.sleep(0.4)
              pyautogui.keyUp('B')
          except Exception as e:
            print(f"An error occurred: {str(e)}")
            
        # another comment
        elif len(hands)==1:
          try:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255
            imgCrop = img[y-offset:y+h+offset,x-offset:x+w+offset]
            # imgCropShape = imgCrop.shape
            aspectRatio = h/w
            if aspectRatio >1:
              k = imgSize/h
              wCal = math.ceil(k*w)
              # time.sleep(.1)
              try:
                imgResize = cv2.resize(imgCrop,(wCal,imgSize))
              except cv2.error as resize_error:
                print("Error")
              # imgResizeShape = imgResize.shape
              wGap = math.ceil((imgSize-wCal)/2)
              imgWhite[:,wGap:wCal+wGap] = imgResize
              prediction,index = classifier.getPrediction(imgWhite)
              print(prediction,labels[index])
            else:
              k = imgSize/w
              hCal = math.ceil(k*h)
              try:
                imgResize = cv2.resize(imgCrop,(imgSize,hCal))
              except cv2.error as resize_error:
                print("Error")
              # imgResizeShape = imgResize.shape
              hGap = math.ceil((imgSize-hCal)/2)
              imgWhite[hGap:hCal+hGap,:] = imgResize
            cv2.imshow("Image", imgWhite)
            
          except Exception as e:
            print(f"An Error occured: {str(e)}")
        
            
        # key = cv2.waitKey(1)
        # if key == ord("m"):
        #   if len(hands)==2:
        #     counter += 1
        #     cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgCombined)
        #     print(counter)
        #   elif len(hands)==1:
        #     counter += 1
        #     cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        #     print(counter)
        
  except Exception as e:
        print(f"An error occurred: {str(e)}")
handDetect()
