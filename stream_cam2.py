#! /usr/bin/env python

import cv2
import numpy as np
import screengrab
import cv2.cv as cv


def main_loop(cv_cap):
    cv2.namedWindow("stream_win")
    cv2.namedWindow("desktop")
    cv2.namedWindow("cam_im")

    chess_im = cv2.imread('chess.png')
    chess_im = cv2.cvtColor(chess_im, cv2.COLOR_RGB2GRAY)

    while True:
        #pi = ImageGrab.grab()
        # Transform ImageGrab image to CV2 standard
        #im_screen = cv2.cvtColor(np.asarray(pi), cv2.COLOR_RGB2BGR)

        r, im = cv_cap.read()

        # extracts the red color channel.
        im_split = cv2.split(im)[2]
        r, imtresh = cv2.threshold(im_split, 150, 255, cv2.THRESH_BINARY)

        im_harris = cv2.cornerHarris(chess_im, 5, 1, 0.04)
        cv2.imshow("stream_win", im_harris)
        cv2.imshow("desktop", chess_im)
        cv2.imshow("cam_im", im)
        if (cv2.waitKey(10) == 27):
            break


def cleanup(cv_cap):
    cv_cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cv_cap = cv2.VideoCapture()

    cv_cap.open(-1)

    if (not cv_cap.isOpened()):
        cleanup(cv_cap)

    try:
        main_loop(cv_cap)
    except Exception, e:
        raise e
    finally:
        cleanup(cv_cap)
