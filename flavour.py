#!/bin/python3 

import mapfrag.structure as mfs 
import mapfrag.read as mfr 

"""
Collection of helper functions for flavour recognition of matrix elements.
"""

################# Reading from MElibrary/MElibrary.map ###################

def read_MElibrary(MEpath):
    MEpath += "/MElibrary.map"
    f = open(MEpath, "r")
    flist = f.readlines()[21:710]
    MElist = []
    Flavlist = []
    for el in flist:
        if mfr.checkline(el):
            elsplit = el.split("=")
            elsplit = [x.strip() for x in elsplit]
            #print("before: ", el)
            #print("after: ", elsplit)
            MElist.append(elsplit[0])
            Flavlist.append(elsplit[1].rsplit("]", 1)[0] + "]")
    return [{"me":me, "flav_string":plist} for me, plist in zip(MElist, Flavlist)] 

def get_flavlist(flav_string):
    return flav_string[1:-1].split(",")

def get_partons(flavlist):
    part = flavlist.copy()
    try:
        part.remove("99")
    except ValueError:
        pass
    try:
        part.remove("-99")
    except ValueError:
        pass 
    try:
        part.remove("98")
    except ValueError:
        pass 
    try:
        part.remove("-98")
    except ValueError:
        pass 
    return part

def reverse_flav(flavlist):
    newflavlist = []
    for el in flavlist:
        if el == "q":
            newflavlist.append("-q")
        elif el == "-q":
            newflavlist.append("q")
        elif el == "0":
            newflavlist.append(el)
        elif el == "Q":
            newflavlist.append("-Q")
        elif el == "-Q":
            newflavlist.append("Q")
        elif el == "99" or el == "-99":
            newflavlist.append(el)
        elif el == "98" or el == "-98":
            newflavlist.append(el)
    return newflavlist 

################## Associate labels in fullme and flavour from MElibrary ########

def apply_label(labels, flavlist):
    
    return None 

