from ctypes import *

# how to use windows dll in python
msvcrt = cdll.msvcrt
msvcrt.printf(b"Hello world\n")
