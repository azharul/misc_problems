#!/usr/bin/python

"""
assume each image is a 2D matrix. When rotate by 90 degrees, convert columns in rows and rows in columns(transpose of matrix). When rotate 180 degrees, then 0*0 element becomes 3*3, 0*3 becomes 3*0 and so on
"""
#rotate an image by 90 degrees
# if we use numpy, transpose is easy, b=a.T
# we want to do it in the old fashioned way

def img_rotate(img1):
	#getting the rows and columns
	rows=len(img1) 
	cols=len(img1[0])
	img2= [[None for i in range(rows)] for i in range(cols)]
	for i  in range(rows):
		for j in range(cols):
			img2[j][i]=img1[i][j]
	return img2

a=[[0,1,2,3],[4,5,6,7],[8,9,10,11]]
print "before rotation=",a
print "after rotation=",img_rotate(a)
