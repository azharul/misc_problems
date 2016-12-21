#!/usr/bin/python

#print out all the combination of 3 digit numbers with no duplicate, ex. 012, 013, ....123, 124, 125...  

import itertools as it

def no_duplicate():
	num=[i for i in range(10)]
	# the following line creates all possible combinations with no duplicates, too easy if I use itertools
	print list(it.combinations(num,3))

no_duplicate() 	

