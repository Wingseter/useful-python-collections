from ctypes import *
from dataclasses import dataclass

# old but more "C" ways
class c_struct1(Structure):
    _fields_ = [
        ("amt_1", c_int),
        ("amt_2", c_int)
    ]

# new and python ways
@dataclass
class c_struct2:
    amt_1: c_int
    amt_2: c_int = 0

p1 = c_struct1(1, 2)
p2 = c_struct2(1, 2)

print(f"{p1.amt_1} {p1.amt_2}")
print(p2)

