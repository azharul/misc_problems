#!/usr/bin/python

#Implement a class that can calculate the running average of a stream of input numbers up to a maximum of N numbers

def running_avg():
	temp=0
	avg=0
	C=1
	n=int(raw_input("Enter maximum number of entries: "))
	while C<=n:
		temp=int(raw_input("Enter number: ")
		avg = (avg*(C-1)+temp)/C
		C +=1
		print avg
	
	if C==n:
		print "your count has ended"

running_avg()
