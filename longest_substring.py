#!/usr/bin/python
# finding longest common substring between two strings
# Note: it can only find longest substring from the beginning or from the end, no matching for strings in the middle
# using iteration

def lcs_iter(str1,str2):	
	longest_common=[0]
	count=0
	# ensuring str1 is always larger or equal to str2
	if len(str2)>len(str1):
		temp=str2
		str2=str1
		str1=temp
	
	#iterating in forward direction of str2	
	for i in range(len(str2)):
		for j in range(len(str1)):
			if str2[i:]==str1[j:j+len(str2[i:])]:
				print str1[j:j+len(str2[i:])]
				longest_common.append(len(str2[i:]))
				break
		else:
			continue
		break
	#iterating in backward direction of str2
	for i in range(len(str2)):
		for j in range(len(str1)):
			if str2[:i]==str1[j:j+len(str2[:i])]:
				print str1[j:j+len(str2[:i])]
				longest_common.append(len(str2[:i]))
				break
		else:
			continue
		break

	print longest_common
	return max(longest_common)	

a="Engineering"
b="YouAreMoreThanDiamondMoreThanGold"
c="snakeDiamond"
d="sringing"
print "length of longest common substring=",lcs_iter(c,b)
