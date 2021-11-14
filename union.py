from ctypes import *
from dataclasses import dataclass

# old but more "C" ways
class c_union1(Union):
    _fields_ = [
        ("amt_1", c_int),
        ("amt_2", c_char * 8)
    ]

value = input("input: ")
p1 = c_union1(int(value))

# it show different type in same memory
print(f"{p1.amt_1} {p1.amt_2}") 


