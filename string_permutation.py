#!/usr/bin/python

#Given a string, print out a permutation of the string in which no two characters next to each other are the same

from itertools import permutations

string="abc"
comb=permutations(string)
for x in comb:
	print ''.join(x)
		
