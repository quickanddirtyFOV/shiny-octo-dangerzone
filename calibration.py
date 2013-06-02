#! /usr/bin/env python

import os
import cv2
import numpy as np
import screengrab
import cv2.cv as cv

from IPython import embed
import pylab as pl

from optparse import OptionParser

def find_line(im, corners, axis = 0):
    if axis == 0:
        first = 0
        second = 1
    else:
        first = 1
        second = 0
    ind = np.lexsort((corners[:, second], corners[:,first]))

    corners = corners[ind]
    median_idx = corners.shape[0] / 2
    median_corner = corners[median_idx, :]
    cv2.circle(im, tuple(median_corner), 10, 0)
    p = np.polyfit((corners[median_idx-1, 0], corners[median_idx, 0]),
                   (corners[median_idx-1, 1], corners[median_idx, 1]),
                   1)
    xmin=0
    xmax=im.shape[1]
    ymin = np.int(np.polyval(p, xmin))
    ymax = np.int(np.polyval(p, xmax))
    cv2.line(im, (xmin, ymin), (xmax, ymax), 0)

    return p


if __name__ == "__main__":
    im = cv2.imread("im_cal.png")
    im = cv2.cvtColor(im, cv.CV_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(im, 11*17, 0.01, 10).squeeze()

    # X direction line, sort corners in Y then X direction
    px = find_line(im, corners, 0)
    # Y direction line, sort corners in X then Y direction
    py = find_line(im, corners, 1)
    print px[0]
    print py[0]

    A = np.array([[px[0], -1],
                 [py[0], -1]])
    z = np.array([[-px[1]],
                 [-py[1]]])
    isect = np.linalg.solve(A, z).squeeze()
    isect = np.round(isect).astype(np.int32)
    cv2.circle(im, tuple(isect), 10, 255)

    for c in corners:
        cv2.circle(im, tuple(c), 5, 127)

    pl.imshow(im, cmap='gray')

    pl.show()
