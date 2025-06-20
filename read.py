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

def checkline(line):
    """A simple routine for checking if the line is suitable for parsing"""
    line = line.strip()
    if len(line) == 0:
        return False
    if line[0] == '#':
        return False
    return True

def clean_line(line):
    line = line.strip()
    return line.rstrip()

def clean_lines(lines):
    newlines = []
    for line in lines:
        newlines.append(clean_line(line))
    return newlines

def readfile(name):
    f = open(name,'r')
    text = f.readlines()
    text = clean_lines(text)
    f.close()
    return text

def readfiles(name_list):
    text = []
    for name in name_list:
        f = open(name, "r")
        text += clean_lines(f.readlines())
        f.close()
    return text

####################### from subtraction terms to their compomnents ###########

def get_sign_from_ant(ant_list):
    sign = ""
    for ant in ant_list:
        if ant[0] == "+" or ant[0] == "-":
            ant_index = ant_list.index(ant)
            ant_list[ant_index] = ant[1:]
            sign = ant[0] + "1"
    return sign, ant_list  #if sign == "" -> there is a coeff != +-1

def get_coeff(subsplit, subdict): #to apply after the other get_something
    for a in subdict["ant"]:
        subsplit.remove(a)
    subsplit.remove(subdict["redme"])
    subsplit.remove(subdict["jet"])
    subsplit.remove(subdict["index"])
    if subsplit != []:
        return subsplit[0]
    else:
        sign, subdict["ant"] = get_sign_from_ant(subdict["ant"])
        return sign

def check_ant(comp):  #notation taken from maple/notation.map
    allowed_ant = readfiles(["ANTlibrary/Lant30IFset.txt", "ANTlibrary/Lant30IIset.txt", "ANTlibrary/Lant30FFset.txt"])
    found_ant = False
    for ant in allowed_ant:
        if ant in comp:
            found_ant = True
    return found_ant

def get_ant(subsplit):
    ant_list = []
    found_ant = False
    for elem in subsplit:
        if check_ant(elem):
            found_ant = True
            ant_list.append(elem)
    if found_ant:
        return ant_list
    else:
        print("Didn't find any antenna or not included in the allowed_ant")
        sys.exit()

def check_redme(comp):
    allowed_redme = readfile("MElibrary/mat40set.txt") #to add and put separately, temporary
    found_redme = False
    for redme in allowed_redme:
        if redme in comp:
            found_redme = True
    return found_redme

def get_redme(subsplit):
    found_redme = False
    for elem in subsplit:
        if check_redme(elem):
            found_redme = True
            return elem
    if not found_redme:
        print("Didn't find reduced matrix element or not included in the allowed_redme")
        sys.exit()

def get_jet(subsplit):
    for elem in subsplit:
        if "JET" in elem:
            return elem

def get_index(subsplit):
    for elem in subsplit:
        if "a" in elem:     #too simple?
            return elem

def break_subterm(subterm):
    subsplit = subterm.split("*")
    subdict = {"ant":get_ant(subsplit), "redme":get_redme(subsplit), "jet":get_jet(subsplit), "index":get_index(subsplit)}
    coeff = get_coeff(subsplit, subdict)
    subdict["coeff"] = coeff
    return subdict

def break_subterms(subterm_list):
    TERMS = []
    for term in subterm_list:
        TERMS.append(break_subterm(term))
    return TERMS

def read_fullme(lines):
    for line in lines:
        if "FN:=" in line:
            return line

#####################  apply labeling ##########################################

def apply_labeling():
    pass



###################### from maple to subtractions terms ########################

def read_SNLO(mapfile):
    f = open(mapfile, "r")
    lines = f.readlines()
    #print(lines)

    lines = remove_comments(lines)
    lines = remove_empty(lines)
    lines = clean_lines(lines)
    #print(lines)

    #get fullme
    fullme_header = read_fullme(lines)

    index_of_xx = next((i for i, elem in enumerate(lines) if "XX" in elem), None)
    #print(index_of_xx)
    terms = lines[index_of_xx+1:-1]

    terms_dict = break_subterms(terms) #coefficients still missing!!!

    return fullme_header, terms_dict

def read_TNLO(mapfile):

    return terms
