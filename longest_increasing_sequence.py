#!/usr/bin/python

#find the longest increasing sequence (LIS) in an array. For example, the length of the LIS for { 16, 22, 13, 33, 22, 33, 41, 62, 75 } is 6 and the longest increasing subsequence is {13, 22, 33, 41, 62, 75}. 

#using dynamic programming, O(n^2) time
def longest_subsequence_dynamic(arr):
	length=[1]*len(arr)
	for j in range(1,len(arr)):
		count=1
		for i in range(0,j):
			# the longest subsequence is found in here. if previous element is smaller than current element AND subseq length of current element is larger or equal to current element, then we increase current length by one. the second part of the if(the and part) is to ensure that the subsequence is maintained in an increasing manner.
			if arr[i]<arr[j] and length[j]<=length[i]:
				length[j] +=1

	return max(length)

# binary search, doing it in O(nlogn) time, wikipedia method
def longest_subsequence_bin(X):
	N = len(X)
	P = [0] * N
	M = [0] * (N+1)
	L = 0
	for i in range(N):
		lo = 1
		hi = L
		while lo <= hi:
			mid = (lo+hi)//2
			if (X[M[mid]] < X[i]):
				lo = mid+1
			else:
				hi = mid-1
 
		newL = lo
		P[i] = M[newL-1]
       		M[newL] = i
 
       		if (newL > L):
           		L = newL
 
    	S = []
    	k = M[L]
    	for i in range(L-1, -1, -1):
        	S.append(X[k])
        	k = P[k]
    	return len(S[::-1])



a=[1,3,2,6,4,5,1]
b=[3,4,-1,0,6,2,3]
c=[15, 27, 14, 38, 26, 55, 46, 65, 85]
print "Longest subsequence using dynamic programming[O(n^2)]",longest_subsequence_dynamic(c)
print "Longest subsequence using binary search[O(nlongn)]",longest_subsequence_bin(c)	
