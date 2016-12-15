#!/usr/bin/python

#Return the max k numbers from an unsorted integer array. #Each number in the array is in the range [0, 10000)

import random

def max_k(arr,k):
	max_num=[]
	for i in range(k):
		max_num.append(max(arr))
		arr.pop(arr.index(max(arr)))
	return max_num

arr=random.sample(range(0,100),20)
k=4

print "generated array",arr
print "first",k,"elements of array=",max_k(arr,k)
