#! /usr/bin/env python

import cv2

if __name__ == "__main__":
    cv_cap = cv2.VideoCapture(0)
    
    cv2.namedWindow("stream_win")
    cv_cap.open(-1)
    prop = cv_cap.get(cv2.cv.CV_CAP_PROP_EXPOSURE)
    print "Eposure time: %d" % prop
    cv_cap.set(cv2.cv.CV_CAP_PROP_EXPOSURE, 100)
    while True:
        r = cv_cap.set(cv2.cv.CV_CAP_PROP_EXPOSURE, 100)
        prop_exp = cv_cap.get(cv2.cv.CV_CAP_PROP_EXPOSURE)
        prop_gain = cv_cap.get(cv2.cv.CV_CAP_PROP_GAIN)

        print "Eposure time: %d %d %d" % (prop_exp, prop_gain, r)
        r, im = cv_cap.read()
        cv2.imshow("stream_win", im)
        if (cv2.waitKey(10) == 27):
            cv_cap.release()
            break

    cv2.destroyAllWindows()
