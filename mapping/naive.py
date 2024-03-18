#!/bin/python3 

import os, sys 
from mapfrag.structure import SubMap 

"""
Implementation of the "naive approach" for J->h mapping
"""

##################### basic steps of the algo ####################

def replace_ant(ant, p_frag):
    if p_frag == "i" or p_frag == "j":
        return ant.replace(p_frag, "3")
    else:
        print("Trying to fragment particle {} in antennae and not allowed".format(p_frag))
        sys.exit()

def replace_redme(redme, p_frag):
    if p_frag == "i" or p_frag == "j":
        return redme.replace(p_frag, "3")
    else:
        print("Trying to fragment particle {} in redme and not allowed".format(p_frag))
        sys.exit()

def replace_jet(jet, p_frag):
    if p_frag == "i" or p_frag == "j":
        jet_arg = jet[5:] #do not consider the first 5 characters, JET11 or similar
        jet_frag = jet[:5] + jet_arg.replace(p_frag, "3") #da aggiustare hfrag(3) o hfrag([3]) in base a cosa?
        return jet_frag 
    else:
        print("Trying to fragment particle {} in jet and not allowed".format(p_frag))
        sys.exit()

def replace_dict(subdict, p_frag):
    newdict = {"ant":[], "redme":"", "jet":"", "index":"", "coeff":""}
    for ant in subdict["ant"]:
        newdict["ant"].append(replace_ant(ant, p_frag))
    newdict["redme"] = replace_redme(subdict["redme"], p_frag)
    newdict["jet"] = replace_jet(subdict["jet"], p_frag)
    newdict["index"] = subdict["index"]
    newdict["coeff"] = subdict["coeff"]
    return newdict 

def replace_frag(subdict_list, p_frag):
    newlist = []
    for subdict in subdict_list:
        newlist.append(replace_dict(subdict, p_frag))
    return newlist

def remove_frag(subdict_list):
    for subdict in subdict_list:
        if "3" not in subdict["jet"]:
            subdict_list.remove(subdict)
    return subdict_list 

#################### B-type ######################################

def replace_Btype(submap):
    subterms_frag = replace_frag(submap.get_subterms(), "i") #first step: particle i now fragment, so "i" -> "3"
    subterms_frag = remove_frag(subterms_frag) #second step: remove subterms if 3 not in JET, i.e. fragmenting particle goes unresolved

    outfile = submap.get_mapname() + "_g.map" #we are assuming we know the flavour of the fragmenting particle, to be recognized automatically
    newfullme = submap.get_fullme() + "_g" #not correct 
    submap_frag = SubMap(submap.get_mapname(), subterms = subterms_frag, outfile = outfile, fullme = newfullme)
    return submap_frag

def replace_Ctype():


    return None 


