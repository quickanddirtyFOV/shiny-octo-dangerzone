#! /usr/bin/env python

import cv

if __name__ == "__main__":
    cv_cap = cv.CaptureFromCAM(0)
    
    cv.NamedWindow("stream_win")

    while True:
        im = cv.QueryFrame(cv_cap)
        cv.ShowImage("stream_win", im)
        if (cv.WaitKey(20) == 27):
            break

    cv.DestroyAllWindows()
