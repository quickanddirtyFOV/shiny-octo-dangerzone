shiny-octo-dangerzone
=====================

How to push to master:

# Add what should be commited
git add -u

# commit
git commit

# push upstream
git push -u origin master

# Installing OpenCv on Linux
# 1. first install these:

    python-opencv
    libhighgui2.3
    libhighgui-dev
    ffmpeg
    libgstreamer0.10-0
    libv4l-0
    libv4l-dev
    libxine2
    libunicap2
    libdc1394-22

# 2.Then follow instructions here:
http://docs.opencv.org/doc/tutorials/introduction/linux_install/linux_install.html

However use the following command for cmake to configure V4L and python correctly

cmake -D CMAKE_BULD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_PYTHON_SUPPORT=ON USE_V4L=ON WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON USE_GStreamer=ON <OpenCV-SRCPATH>
