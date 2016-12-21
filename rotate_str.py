#!/usr/bin/python

#rotate a string, find several solutions

#using iteration
def rotate_string(string):
	rotated=[]
	for i in range(len(string)):
		rotated.append(string[len(string)-1-i])

	return ''.join(rotated)

A="beat thy beast"
print A
print rotate_string(A)
