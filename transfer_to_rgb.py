# This is the script to apply different Image Enhancement Technics

import cv2
import os
from src.algorithms.runner import AlgorithmRunner

folder_train = "/Users/siyiwei/Desktop/x-ray-images-enhancement/images/512hef/train"
rgb_train = "/Users/siyiwei/Desktop/x-ray-images-enhancement/images/512rgb/train"

folder_test = "/Users/siyiwei/Desktop/x-ray-images-enhancement/images/512hef/test"
rgb_test = "/Users/siyiwei/Desktop/x-ray-images-enhancement/images/512rgb/test"

ar = AlgorithmRunner("hef", rgb_train, folder_train)
ar.run()

ar = AlgorithmRunner("hef", rgb_test, folder_test)
ar.run()