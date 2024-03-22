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
        self.fullme_name = self.get_fullme_name()
        self.fullme_particles = self.get_fullme_particles()

    def read(self):
        if "SNLO" in self.name:
            self.fullme, self.subterms = mfr.read_SNLO(self.mapfile)
        else: 
            print("Matrix element type does not exist or not implemented yet")
            sys.exit()
    
    def get_fullme(self):
        return self.fullme

    def get_mapname(self):
        return self.name

    def get_mapfile(self):
        return self.mapfile

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

    def make_submap(self, new_subterms):
        self.subterms = mfr.break_subterms(new_subterms)
        return self.subterms

    def update_subterms(self, newsubterms):
        self.subterms = newsubterms 
        return None

    def define_outfile(self, outfile):
        self.outfile = outfile 
        return None 


    def define_fullme(self, fullme):
        self.fullme = fullme 
        return None 

    def define_mapname(self, mapname):
        self.name = mapname 
        return None

    def get_fullme_name(self):
        return self.fullme[self.fullme.find("=")+1:self.fullme.find("(")]

    def get_fullme_particles(self):
        return self.fullme[self.fullme.find("("):self.fullme.find(":", self.fullme.find("("))]

    def get_particles(self):
        return self.get_fullme_particles()[1:-1].split(",")

    def get_initial_state(self):
        return self.get_particles()[:2]

    def get_final_state(self):
        return self.get_particles()[2:]

    def get_final_state_partons(self):
        fs = self.get_final_state()
        for p in ["Z", "H", "W"]:   #gamma is missing
            try:
                fs.remove(p)
            except ValueError:
                pass 
        return fs 

class SubTerm():
    def __init__(self, subdict):
        self.subdict = subdict 

    def get_particles():

        return None 

class ME(): #class for ME, also redme are ME 
    def __init__(self, me_string):
        self.me_string = me_string

    def get_particles(self):
        return self.me_string[self.me_string.find("(")+1:self.me_string.find(")")].split(",")

    def get_me(self):
        return self.me_string[:self.me_string.find("(")]

    def replace_particle(self):
        return None 


class Ant(): #class for antennae
    def __init__(self, ant_string):
        self.ant_string = ant_string 
       # self.ant = #name of the ant 

class Jet():
    def __init__(self, jet_string):
        self.jet_string = jet_string






