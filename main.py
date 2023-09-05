# Libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests as req

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Contruct an object
class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        s = f"{self.re} + i{self.im}"
        return s

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.re == other.re and self.im == other.im
        else:
            raise Exception(f"{other} is not an instance of ComplexNumber")

    def __setitem__(self, k, v):
        if k not in ["re", "im"]:
            raise Exception(f"{k} is not a vil key for ComplexNumber")
        elif k == "re":
            self.re = v
        elif k == "im":
            self.im = v

    def __getitem__(self, k):
        if k not in ["re", "im"]:
            raise Exception(f"{k} is not a vil key for ComplexNumber")
        elif k == "re":
            return self.re
        elif k == "im":
            return self.im
          
    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re + other.re, self.im + other.im)
        elif isinstance(other, int):
            return ComplexNumber(self.re + other, self.im + other)
        elif isinstance(other, float):
            return ComplexNumber(self.re + other, self.im + other)
        else:
            raise Exception(f" {type(other)} {other} isn't a valid type")
        
    def __len__(self):
        from math import sqrt
        return int(sqrt(self.re**2 + self.im**2))

# initialise the object ComplexNumber
c1 = ComplexNumber(5, 6)
print(c1)

c2 = ComplexNumber(5, 6)
print(c2)
# try various methods
print(c1)
print(c1 + 1)
print(c1 + c2)
print(c1 + "s")
c1["re"] = 55
print(len(c1))