#!/usr/bin/python

"""
You are given a 2d rectangular array of positive integers representing the height map of a continent. The "Pacific ocean" touches the left and top edges of the array and the "Atlantic ocean" touches the right and bottom edges. 
- Find the "continental divide". That is, the list of grid points where water can flow either to the Pacific or the Atlantic. 
Water can only flow from a cell to another one with height equal or lower. 

Example: 

Pacific ~ ~ ~ ~ ~ |__ 
~ 1 2 2 3 (5) ~ 
~ 3 2 3 (4)(4) ~ 
~ 2 4 (5) 3 1 ~ 
~ (6)(7) 1 4 5 ~ 
__ (5) 1 1 2 4 ~ 
|~ ~ ~ ~ ~ Atlantic 

The answer would be the list containing the coordinates of all circled cells: 
[(4,0), (3,1), (4,1), (2,2), (0,3), (1,3), (0,4)]


"""

import numpy as np

#function to finnd the "continental divide"
def continental_divide(mat):
	num=0
	for row in mat:
		num +=1
		print str(num),str(np.where(row==max(row)))


#continent height map
matrix=np.array([[1,2,3,4,5], [3,2,3,4,4], [2,4,5,2,1], [6,7,1,4,5], [5,1,1,3,4]])
continental_divide(matrix)
