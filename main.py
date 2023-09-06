# Libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests as req

# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# # Contruct an object to test Dunder Methods (double underscore methods)
# class ComplexNumber:
#     def __init__(self, re, im):
#         self.re = re
#         self.im = im

#     def __str__(self):
#         s = f"{self.re} + i{self.im}"
#         return s

#     def __eq__(self, other):
#         if isinstance(other, ComplexNumber):
#             return self.re == other.re and self.im == other.im
#         else:
#             raise Exception(f"{other} is not an instance of ComplexNumber")

#     def __setitem__(self, k, v):
#         if k not in ["re", "im"]:
#             raise Exception(f"{k} is not a vil key for ComplexNumber")
#         elif k == "re":
#             self.re = v
#         elif k == "im":
#             self.im = v

#     def __getitem__(self, k):
#         if k not in ["re", "im"]:
#             raise Exception(f"{k} is not a vil key for ComplexNumber")
#         elif k == "re":
#             return self.re
#         elif k == "im":
#             return self.im
          
#     def __add__(self, other):
#         if isinstance(other, ComplexNumber):
#             return ComplexNumber(self.re + other.re, self.im + other.im)
#         elif isinstance(other, int):
#             return ComplexNumber(self.re + other, self.im + other)
#         elif isinstance(other, float):
#             return ComplexNumber(self.re + other, self.im + other)
#         else:
#             raise Exception(f" {type(other)} {other} isn't a valif type")
        
#     def __len__(self):
#         from math import sqrt
#         return int(sqrt(self.re**2 + self.im**2))

# # initialise the object ComplexNumber
# c1 = ComplexNumber(5, 6)
# print(c1)

# c2 = ComplexNumber(5, 6)
# print(c2)
# # try various methods
# print(c1)
# print(c1 + 1)
# print(c1 + c2)
# print(c1 + "s")
# c1["re"] = 55
# print(len(c1))
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Private attribute and name Mangling
# class Pearson():
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#     def __str__(self) -> str:
#         return f"{self.firstName} {self.lastName}"
    
# class PrivatePearson(Pearson):
#     def __init__(self, firstName, lastName, privateInfo):
#         super().__init__(firstName, lastName)
#         self.__privateInfo = privateInfo
    
#     def __str__(self) -> str:
#         return super().__str__() + f" {self.__privateInfo}"

# p1 = Pearson("Manuel", "Chiocchetta")

# print(p1)

# p1.firstName="Carlo"
# print(p1)

# p2Private = PrivatePearson("Manuel", "Chiocchetta", "SecretInfo")
# print(p2Private)

# p2Private.__privateInfo = "NewSecret"
# print(dir(p2Private))

# p2Private._PrivatePearson__privateInfo = "NewSecret"
# print(p2Private)
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Exceptions

# import inspect

# def exception_tree(cls, ind = 0):
#     print("-" * ind, cls)
#     for i in cls.__subclasses__():
#         exception_tree(i, ind + 2)
        


# exception_tree(BaseException)
# °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
# Game 1 (sasso, carta, forbici)

import random

occurrences = {
    "sasso": 0,
    "carta": 0,
    "forbice": 0
}

for i in range(1000):

    r = random.randint(0,2)
    if r == 0:
        occurrences["sasso"] += 1
    if r == 1:
        occurrences["forbice"] += 1
    if r == 2:
        occurrences["carta"] += 1

print(occurrences)