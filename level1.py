import cv2
from color_recognition_api import color_histogram_feature_extraction
from color_recognition_api import knn_classifier
#import pp
import os
import os.path
import pygame
import math
import numpy as np
import time




pygame.init()



cap = cv2.VideoCapture(1)
(ret, frame) = cap.read()
prediction = 'n.a.'






# checking whether the training data is ready
PATH = './training.data'


if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print ('training data is ready, classifier is loading...')
else:
    print ('training data is being created...')
    open('training.data', 'w')
    color_histogram_feature_extraction.training()
    print ('training data is ready, classifier is loading...')





while True:

    # Capture frame-by-frame
    (ret, frame) = cap.read()

    cv2.putText(
        frame,
        'Prediction: ' + prediction,
        (15, 45),
        cv2.FONT_HERSHEY_PLAIN,
        3,
        200,
        )

    # Display the resulting frame

    cv2.imshow('color classifier', frame)

    color_histogram_feature_extraction.color_histogram_of_test_image(frame)

    prediction = knn_classifier.main('training.data', 'test.data')


    #pp.main()

    if(prediction=='black'):
     s = pygame.mixer.Sound("b.wav")
     s.play()

    if(prediction=='white'):
      s = pygame.mixer.Sound("c.wav")
      s.play()


    if(prediction=='blue'):
      s = pygame.mixer.Sound("a.wav")
      s.play()



    if(prediction=='green'):
      s = pygame.mixer.Sound("g.wav")
      s.play()



    if(prediction=='yellow'):
      s = pygame.mixer.Sound("f.wav")
      s.play()




    if(prediction=='orange'):
      s = pygame.mixer.Sound("e.wav")
      s.play()


    if(prediction=='red'):
      s = pygame.mixer.Sound("d.wav")
      s.play()


    if(prediction=='brown'):
      s = pygame.mixer.Sound("eb.wav")
      s.play()







    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
import main.py





# When everything done, release the capture
