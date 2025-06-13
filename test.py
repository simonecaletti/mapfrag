#!/usr/bin/env python3

# Test script for the read library.
#

from read import clean_lines, readfile, remove_comments, remove_empty
import read

path = "/home/simone/hepsoftware/NNLOJET/maple/process/epemjj/"
filename = "B1g0ZepemjjSNLO.map"

# Declare here the labeling of the real. Last is the extra emission.
# The RedME and Ant labeling have to be declared separately in this file.
# Labels are given with PDG codes, or q/qb for generic quarks.
FullSNLO_labeling = [ep, em, qb, g, q]
Ant_labeling = [qb, g, q]
RedME_labeling = [qb, q, ep, em]

# Note: check the Atn  and RedME in the test file are in the corresponding libraries
head, dict = read.read_SNLO(path + filename)
print(dict)
