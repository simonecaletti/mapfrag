#!/bin/python3 

import os, sys
from mapfrag.read import read_SNLO

"""
python class for maple subtraction terms
"""

class SubMap:
    def __init__(self, name):
        self.name = name
        self.mapfile = name + ".map"
        self.subterms = []

    def read(self):
        if "SNLO" in self.name:
            self.fullme, self.subterms = read_SNLO(self.mapfile)
        else: 
            print("Matrix element type does not exist or not implemented yet")
            sys.exit()

    def get_subterm(self, i):
        return self.subterms[i]
        
    def get_subterms(self):
        return self.subterms

    def combine_subterm():

        return None

    def combine_subterms():

        return None
