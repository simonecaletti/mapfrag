#!/bin/python3 

import os, sys 
from mapfrag.structure import SubMap
import re 

"""
Implementation of the "naive approach" for J->h mapping
"""

##################### basic steps of the algo ####################

def frag_in_square(jet, p_frag):
    found_square = False
    if re.search("\[.," + p_frag + "\]", jet) or re.search("\[" + p_frag + ",.\]", jet):
        found_square = True
    #print(jet, found_square)
    return found_square 

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
    #print("JET:", jet)
    if p_frag == "i" or p_frag == "j":
        jet_arg = jet[5:] #do not consider the first 5 characters, JET11 or similar
        if frag_in_square(jet_arg, p_frag):
            #print("JETARG:", jet_arg)
            jet_frag = jet[:5] + "(hfrag" + jet_arg[:jet_arg.index("[")] + "[3])" + jet_arg[jet_arg.index("]")+1:] #from hfrag([i, j]) to hfrag([3])
        else:
            #print("JETARG:", jet_arg)
            jet_frag = jet[:5] + jet_arg.replace(p_frag, "hfrag(3)") #from hfrag(i) to hfrag(3) 
    else:
        print("Trying to fragment particle {} in jet and not allowed".format(p_frag))
        sys.exit()
    #print(jet_frag)
    return jet_frag 

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

################## basic functions for fullme ####################

def get_flavour(fullme_name, particles_set, p_frag):
    return "_g" #to be implemented, atm we always return gluon 

def update_fullme_name(submap, p_frag):
    return submap.get_fullme_name() + get_flavour(submap.get_fullme_name(), submap.get_fullme_particles(), p_frag)

def replace_fullme_particles(submap, p_frag):
    oldset = submap.get_fullme_particles()
    newset = oldset.replace(p_frag, "3")
    newset = newset.replace("j", p_frag)
    return newset 

def update_fullme(submap, p_frag):
    fullme_name = update_fullme_name(submap, p_frag)
    particles_set = replace_fullme_particles(submap, p_frag)
    return "FN:=" + fullme_name + particles_set

#################### B-type ######################################

def singlereplace_Btype(submap, p_frag):
    subterms_frag = replace_frag(submap.get_subterms(), p_frag) #first step: particle i now fragment, so "i" -> "3"
    subterms_frag = remove_frag(subterms_frag) #second step: remove subterms if 3 not in JET, i.e. fragmenting particle goes unresolved

    outfile = submap.get_mapname() + "_g.map" #we are assuming we know the flavour of the fragmenting particle, to be recognized automatically
    newfullme = update_fullme(submap, p_frag) #it works, but we always consider the second parton to be j and do j -> i 
    submap_frag = SubMap(submap.get_mapname(), subterms = subterms_frag, outfile = outfile, fullme = newfullme)

    return submap_frag


################### C-type ########################################


def replace_Ctype():


    return None 


##################



