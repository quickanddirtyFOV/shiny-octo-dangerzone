#! /usr/bin/env python

import os
import cv2
import numpy as np
import screengrab
import cv2.cv as cv

from IPython import embed
import pylab as pl

do_embed = True


def main_loop(cv_cap):
    cv2.namedWindow("dbg")
    cv2.namedWindow("desktop")
    cv2.namedWindow("cam")

    im_chess = cv2.imread('chess.png')
    im_chess = cv2.cvtColor(im_chess, cv2.COLOR_BGR2GRAY)

    calibrate = True
    sg = screengrab.screengrab()

    while True:
        # Currently screengrab causing issues with OpenCV in linux.
        if (os.name != "posix"):
            s = sg.screen()
            # Transform PIL image to OpenCV Image
            im_screen = cv2.cvtColor(np.asarray(s), cv2.COLOR_RGB2BGR)
            cv2.imshow("desktop", im_screen)
        else:
            cv2.imshow("desktop", im_chess)

        r, im = cv_cap.read()

        # extracts the red color channel.
        im_split = cv2.split(im)[2]
        r, imtresh = cv2.threshold(im_split, 150, 255, cv2.THRESH_BINARY)

        if (calibrate and os.name != "posix"):
            im_harris = cv2.cornerHarris(im_chess, 5, 1, 0.04)
            cv2.imshow("dbg", im_harris)

        cv2.imshow("cam", im)

        # Get key-press event, this is needed for CV events to be processed.
        k = cv2.waitKey(10)

        if (k == 27):
	    if do_embed:
		embed()
            break
        elif (k == ord('c')):
            print "Toggling calibration"
            calibrate = not calibrate


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
        print e
        raise e
    finally:
        cleanup(cv_cap)
