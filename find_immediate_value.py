#!/usr/bin/python

#Find immediate smallest element in a sorted array given any value recursively

def find_immediate_value(arr,val):
	# if immediate smallest value is in array, then print it
	if val in arr:
		val_pos=arr.index(val)
		print "immediate value", val
		print "position",val_pos
	#else, keep looking recursively
	else:
		find_immediate_value(arr,val-1)

a=[1,3,6,7,8,9,12,13,14,18,19,20,24,25,29,30,34,37,38,40,43,44,47,51]

val1=17
val2=46

find_immediate_value(a,val1-1)
find_immediate_value(a,val2-1)

