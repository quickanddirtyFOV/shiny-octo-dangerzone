
# Needed flags for compiling and linking with opencv
CFLAGS = $(shell pkg-config --cflags opencv)
LDLIBS = $(shell pkg-config --libs opencv)

# Source files
SRCS-y = opencvstart.cc
OBJS = $(SRCS-y:.cc=.o)

# Binary name
PROG   = showim

all:
	$(CXX) $(CFLAGS) $(SRCS-y) -o $(PROG) $(LDLIBS)

clean:
	rm -rf $(PROG)
	rm -rf $(OBJS)
