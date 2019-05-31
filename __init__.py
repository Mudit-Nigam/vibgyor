
import cv2
from color_recognition_api import color_histogram_feature_extraction
from color_recognition_api import knn_classifier
import pp
import os
import os.path
import pygame
import math
import numpy as np
import time




ch=input('Enter 1 for level 1 or 2 for level 2')
if(ch=='1'):
    import level1



if(ch=='2'):
    import level2


else:
   print('Enter correct choice')
