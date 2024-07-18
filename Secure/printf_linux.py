from ctypes import *

# how to use printf linux in python
libc = CDLL("libc.so.6")
libc.printf(b"Hello world")