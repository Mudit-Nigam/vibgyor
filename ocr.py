from PIL import Image
from pytesseract import image_to_string
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



cap = cv2.VideoCapture(0)
(ret, frame) = cap.read()

entire_text=image_to_string(frame,lang='eng')
with open("Output.txt", "w") as text_file:
    text_file.write(entire_text)

import ttos
