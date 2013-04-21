#! /usr/bin/env python

import screengrab

if __name__ == '__main__':
    sg = screengrab.screengrab()

    s = sg.screen()

    s.show()
