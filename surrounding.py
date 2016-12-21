#!/usr/bin/python

#Given an NxN grid of 0s, 1s, and 2s, find out whether 1s or 2s is surrounded starting at (i,j). Being surrounded means that 1s is surrounded by 2s or that 2s is surrounded by 1s

#doing it the hard way(checking every value around a position(i,j)
import random
import numpy as np
def surround(arr):
	m=len(arr)
	n=len(arr[0])
	for i in range(1,m-1):
		for j in range(1,n-1):
			if arr[i][j]==1 and (arr[i-1][j-1]==2 and arr[i-1][j]==2 and arr[i-1][j+1]==2 and arr[i][j-1]==2 and arr[i][j+1]==2 and arr[i+1][j-1]==2 and arr[i+1][j]==2 and arr[i+1][j+1]==2):
				print "array position (",i,",",j,") is surrounded by 2s"
			elif arr[i][j]==2 and (arr[i-1][j-1]==1 and arr[i-1][j]==1 and arr[i-1][j+1]==1 and arr[i][j-1]==1 and arr[i][j+1]==1 and arr[i+1][j-1]==1 and arr[i+1][j]==1 and arr[i+1][j+1]==1):
				print "array position (",i,",",j,") is surrounded by 1s"	

#doing it using numpy
def surround_numpy(arr):
	m=len(arr)
	n=len(arr[0])
	for i in range(m-2):
		for j in range(n-2):
			if np.prod(arr[i:i+3,j:j+3])==256 and arr[i+1,j+1]==1:
				print "array position (",(i+1),",",(j+1),") is surrounded by 2s(numpy)"
			elif np.prod(arr[i:i+3,j:j+3])==2 and arr[i+1,j+1]==2:
				print "array position (",(i+1),",",(j+1),") is surrounded by 1s(numpy)"
#creating an m*n matrix with 0,1,2 randomly generated. Here, m=292, n=281
matrix=[[random.randint(0,2) for i in range(281)] for j in range(292)]
surround(matrix)

#using numpy to generate m*n matrix, m=292,n=281
np_arr=np.array([[random.randint(0,2) for i in range(281)] for j in range(292)])
surround_numpy(np_arr)
