#! /usr/bin/env python

import cv2
import numpy as np
from PIL import ImageGrab
import cv2.cv as cv

if __name__ == "__main__":
    chess_im = cv2.imread('chess.png')
    chess_im = cv2.cvtColor(chess_im, cv2.COLOR_RGB2GRAY)
    cv_cap = cv2.VideoCapture(0)
    
    cv2.namedWindow("stream_win")
    cv2.namedWindow("desktop")
    cv2.namedWindow("cam_im")
    cv_cap.open(-1)
    
    while True:
        pi = ImageGrab.grab()
        #im_cv = np.asarray(pi)[:,:,::-1].copy() # Transform ImageGrab image to CV2 standard
        im_screen = cv2.cvtColor(np.asarray(pi), cv2.COLOR_RGB2BGR) # Transform ImageGrab image to CV2 standard
        
        r, im = cv_cap.read()
        
        im_split = cv2.split(im)[2] # extracts the red color channel.
        r, imtresh = cv2.threshold(im_split, 150, 255, cv2.THRESH_BINARY)
        
        im_harris = cv2.cornerHarris(chess_im, 5, 1, 0.04)
        cv2.imshow("stream_win", im_harris)
        cv2.imshow("desktop", chess_im)
        cv2.imshow("cam_im", im)
        if (cv2.waitKey(10) == 27):
            cv_cap.release()
            break

    cv2.destroyAllWindows()
