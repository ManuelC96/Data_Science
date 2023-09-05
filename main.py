# Libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests as req

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

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


c1 = ComplexNumber(5, 6)
print(c1)

c2 = ComplexNumber(5, 6)
print(c2)

c1["re"] = 55
print(c1)

print(c1["im"])