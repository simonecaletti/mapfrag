#!/bin/python3 

import os, sys
import mapfrag.read as mfr 
import mapfrag.write as mfw

"""
python class for maple subtraction terms
"""

class SubMap:
    def __init__(self, name, subterms = [], outfile="outfile.map", fullme = ""):
        self.name = name
        self.mapfile = name + ".map"
        self.subterms = subterms 
        self.outfile = outfile
        self.fullme = fullme

    def read(self):
        if "SNLO" in self.name:
            self.fullme, self.subterms = mfr.read_SNLO(self.mapfile)
        else: 
            print("Matrix element type does not exist or not implemented yet")
            sys.exit()
    
    def get_fullme(self):
        return self.fullme

    def get_subterm(self, i):
        return self.subterms[i]
        
    def get_subterms(self):
        return self.subterms

    def make_subterm(self, subterm):
        return mfw.make_subterm(subterm)

    def make_subterms(self):
        return mfw.make_subterms(self.subterms)

    def write(self):
        mfw.write_header(self.fullme ,self.outfile)
        mfw.write_subterms(mfw.make_subterms(self.subterms), self.outfile)
        return None
