#!/usr/bin/python
# -*- coding: utf-8 -*-

#Given a sorted array [0-99] With input: [1, 5, 45, 86] Write a function that prints the empty regions, example Output: “0,2-4,6-44,46-85,87-99”

# solution using iteration
def find_empty_region(arr):
	
	for i in range(len(arr)):
		if arr[i] is None:
			print i

a=[None,1,None,None,4,5,None,None,None,9,None,None,None,None,None,15]
find_empty_region(a)
