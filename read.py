#!/bin/python3 

import sys, os

"""
Collection of helper functions for the SubMap class 
"""
######################## basic functions #######################################
def remove_comments(lst):
    clean_list = [elem for elem in lst if not elem.strip().startswith("#")] 
    return clean_list

def remove_empty(lst):
    clean_list = [elem for elem in lst if not elem.strip()==""]
    return clean_list

####################### from subtraction terms to their compomnents ###########

def break_subterm(subterm):
    comp = subterm.split("*")
    comp_dict = {"ant":comp[0], "redME":comp[1], "jet":comp[2]} #too simple, coeff need to be implemented
    return comp_dict 

def break_subterms(subterm_list):
    TERMS = []
    for term in subterm_list:
        TERMS.append(break_subterm(term))
    return TERMS 

###################### from maple to subtractions terms ########################

def read_SNLO(mapfile):
    f = open(mapfile, "r")
    lines = f.readlines()
    #print(lines)
    
    lines = remove_comments(lines)
    lines = remove_empty(lines)
    #print(lines)

    index_of_xx = next((i for i, elem in enumerate(lines) if "XX" in elem), None)
    #print(index_of_xx)
    terms = lines[index_of_xx+1:-1]
    
    terms_dict = break_subterms(terms)

    return terms_dict 

def read_TNLO(mapfile):
    
    return terms 

