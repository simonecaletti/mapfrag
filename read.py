#!/bin/python3 

import sys, os

"""
Collection of helper functions for the SubMap class 
"""

def remove_comments(lst):
    clean_list = [elem for elem in lst if not elem.strip().startswith("#")] 
    return clean_list

def remove_empty(lst):
    clean_list = [elem for elem in lst if not elem.strip()==""]
    return clean_list

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
    return terms

def read_TNLO(mapfile):
    
    return terms 

