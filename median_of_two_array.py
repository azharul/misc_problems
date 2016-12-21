#!/usr/bin/python

# There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n))

def findMedianSortedArrays( A, B):
	if (len(A) + len(B)) % 2 == 0:
		return (fms(A, B, (len(A) + len(B))/2) + fms(A, B, (len(A) + len(B))/2 + 1))/2.0
	else:
          	return fms(A, B, (len(A) + len(B))/2 + 1)
     
def fms(A, B, k):
	if len(A) > len(B):
            	return fms(B, A, k)
        else:
            	if len(A) == 0:
                	return B[k-1]
            	if k == 1:
                	return min(A[0], B[0])
            	pa = min(k/2, len(A))
            	pb = k - pa
            	if A[pa-1] <= B[pb-1]:
                	return fms(A[pa::], B
, k-pa)
            	else:
                	return fms(A, B[pb::], k-pb)
             
arr1=[1,2,3,4]
arr2=[5,6,7,8]

print findMedianSortedArrays(arr1,arr2)
