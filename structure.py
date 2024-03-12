#!/bin/python3 

import os, sys
from read import read_sub

"""
python class for maple subtraction terms
"""

class SubMap:
    def __init__(self, name)
        self.name = name
        self.mapfile = name + ".map"
        self.terms = read_sub(self.mapfile)

    def term(i):
        return self.terms[i]


