shiny-octo-dangerzone
=====================

How to push to master:

# Add what should be commited
git add -u

# commit
git commit

# push upstream
git push -u origin master

# Installing OpenCv 2.4.5 on Linux
# 1. first install these:

    python-opencv
    ffmpeg
    libgstreamer0.10-0
    libv4l-0
    libv4l-dev
    libxine2
    libunicap2
    libunicap2-dev
    libdc1394-22
    mjpeg* packages
    libxine1-dev
    libxine1-ffmpeg
    libtbb-dev
    libtbb2
    cmake-qt-gui
    libqt4* packages
    libopenexr6
    libopenexr-dev

# 2.Then follow instructions here:
http://docs.opencv.org/doc/tutorials/introduction/linux_install/linux_install.html

But using cmake is a real hazzle. From your created cmake_dir, run instead:

$ cmake-gui <opencv_dir>

This will give you a view of what will be built (BUILD_*), some information about where in the system the various packages
where found and also which libraries to use when building (WITH_*). I checked all of the WITH_ except OpenNI and OpenCL
(got some build problem with openCL, if you fix this plz let me know).
I recommend not check any box for building external packages from src e.g BUILD_JASPER, since this will probably screw
up your system.

Also check the ENABLE_* flags. ENABLE_FAST_MATH is nice to have for example.

Clicking "generate" (Unix Makefiles) will try to configure the build with your options. You will get a summary of what will be supported.

Below is my generated output when building. Check that you also have at least everyting enabled as below.
For example I had issues with bad performance and mjpeg not working correclty without tbb and all of the xine/ffmpeg stuff.

If there is some problem with finding a dependency you will get a warning. Most likely a dev-package is missing so just get
it from apt-get.

Once done iterating this, just click configure and exit cmake-gui. Now you can make and install according to the standard
instruction.

Once done installing. Add this to the rc-file of your favorite shell:

export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

As all of the OpenCV libraries are installed into /usr/local/lib. If you decided to use another
install prefix change the link accordingly. 

General configuration for OpenCV 2.4.5 =====================================
  Version control:               unknown

  Platform:
    Host:                        Linux 2.6.32-5-amd64 x86_64
    CMake:                       2.8.2
    CMake generator:             Unix Makefiles
    CMake build tool:            /usr/bin/gmake
    Configuration:               Release

  C/C++:
    Built as dynamic libs?:      YES
    C++ Compiler:                /usr/bin/c++  (ver 4.4.5)
    C++ flags (Release):         -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffast-math -msse -msse2 -msse3 -ffunction-sections -O3 -DNDEBUG  -DNDEBUG
    C++ flags (Debug):           -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffast-math -msse -msse2 -msse3 -ffunction-sections -g  -O0 -DDEBUG -D_DEBUG -ggdb3
    C Compiler:                  /usr/bin/gcc
    C flags (Release):           -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffast-math -msse -msse2 -msse3 -ffunction-sections -O3 -DNDEBUG  -DNDEBUG
    C flags (Debug):             -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffast-math -msse -msse2 -msse3 -ffunction-sections -g  -O0 -DDEBUG -D_DEBUG -ggdb3
    Linker flags (Release):
    Linker flags (Debug):
    Precompiled headers:         YES

  OpenCV modules:
    To be built:                 core imgproc flann highgui features2d calib3d ml video objdetect contrib photo legacy gpu nonfree python stitching superres ts videostab
    Disabled:                    world
    Disabled by dependency:      -
    Unavailable:                 androidcamera java ocl

  GUI: 
    QT 4.x:                      YES (ver 4.6.3 EDITION = OpenSource)
    QT OpenGL support:           NO
    OpenGL support:              NO

  Media I/O: 
    ZLib:                        /usr/lib64/libz.so (ver 1.2.3.4)
    JPEG:                        /usr/lib64/libjpeg.so (ver 62)
    PNG:                         /usr/lib64/libpng.so (ver 1.2.44)
    TIFF:                        /usr/lib64/libtiff.so (ver 42 - 3.9.4)
    JPEG 2000:                   /usr/lib64/libjasper.so (ver 1.900.1)
    OpenEXR:                     /usr/lib64/libImath.so /usr/lib64/libIlmImf.so /usr/lib64/libIex.so /usr/lib64/libHalf.so /usr/lib64/libIlmThread.so (ver 1.6.1)

  Video I/O:
    DC1394 1.x:                  NO
    DC1394 2.x:                  YES (ver 2.1.2)
    FFMPEG:                      YES
      codec:                     YES (ver 52.123.0)
      format:                    YES (ver 52.111.0)
      util:                      YES (ver 50.43.0)
      swscale:                   YES (ver 0.14.1)
      gentoo-style:              YES
    GStreamer:                   NO
    OpenNI:                      NO
    OpenNI PrimeSensor Modules:  NO
    PvAPI:                       NO
    GigEVisionSDK:               NO
    UniCap:                      YES (ver 0.9.5)
    UniCap ucil:                 YES (ver 0.9.5)
    V4L/V4L2:                    Using libv4l (ver 0.8.0)
    XIMEA:                       NO
    Xine:                        YES (ver 1.1.19)

  Other third-party libraries:
    Use IPP:                     IPP not found
    Use Eigen:                   NO
    Use TBB:                     YES (ver 3.0 interface 5000)
    Use OpenMP:                  NO
    Use GCD                      NO
    Use Concurrency              NO
    Use C=:                      NO
    Use Cuda:                    NO
    Use OpenCL:                  NO

  Python:
    Interpreter:                 /usr/bin/python2.6 (ver 2.6.6)
    Libraries:                   /usr/lib64/libpython2.6.so
    numpy:                       /usr/local/lib/python2.6/dist-packages/numpy/core/include (ver 1.7.0)
    packages path:               lib/python2.6/dist-packages

  Java:
    ant:                         NO
    JNI:                         NO
    Java tests:                  YES

  Documentation:
    Build Documentation:         NO
    Sphinx:                      NO
    PdfLaTeX compiler:           /usr/bin/pdflatex

  Tests and samples:
    Tests:                       YES
    Performance tests:           YES
    C/C++ Examples:              YES

  Install path:                  /usr/local

  cvconfig.h is in:              /home/filipj/src/opencv-2.4.5/cmake_binary_dir
-----------------------------------------------------------------

Configuring done
