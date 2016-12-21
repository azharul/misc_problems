#!/usr/bin/python

#Implement a function that takes the set-wise subtraction of two sorted sets of integers. ie A = {1, 2, 3}, B = {3, 4, 5} =&gt; A - B = {1, 2}. There can be duplicates, in which case all duplicates should be removed should there be an occurrence in B. IE: {1, 2, 3, 3, 3} - {2, 3} = {1}. 

from sets import Set
# the following function will get two lists and do the subtractions
def set_subtract(set1,set2):
	set1=Set(set1)
	set2=Set(set2)
	sub=set1-set2
	return sub

A=[1,2,3,3,4,4,5]
B=[4,4,5,5,6,6,7,8,8]
print A
print B
print set_subtract(A,B)
