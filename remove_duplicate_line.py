#!/usr/bin/python

#Give you a text file, remove duplicated lines. Follow up: If the file is very #large, general hashmap takes too much spaces, come up with a better solution

#solving using python file operation
def remove_duplicate_line(filename):
	fo=open(filename,'r')
	lineseen=[]
	#storing lines in a variable
	for line in fo:
		if line not in lineseen:
			lineseen.append(line)
	return lineseen		

file1='textfile.txt'
#print remove_duplicate_line(file1)
remove_duplicate_hash(file1)
