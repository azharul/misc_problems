#!/usr/bin/python
from itertools import izip
#Determine if List C is interleaving of  list A and B
def isInterleaving(C,A,B):
	isInter=True
	for i in range(len(C)):
		if i%2==0:
			if  C[i]!=A[i//2]:
				isInter=False
				print "not interleaving"
				break
		else:
			if C[i]!=B[i//2]:
				isInter=False
				print "not interleaving"
				break
	if  isInter==True:
		print "Interleaving"


#creating an interleaving list
a=[1,2,3]
b=['w','x','y','z']
#b=[1,4,6,3]
#creating an interleaving list
inter=[item for items in izip(a,b) for item in items]

test=[1,2,3,'w','x','y']
isInterleaving(test,a,b)

