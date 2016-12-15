#!/usr/bin/python
#1. A string consists of ‘0’, ‘1’ and '?'. The question mark can be either '0' or '1'. Find all possible combinations for a string
#solved using iteration
def find_comb(string):
	results=["0","1"] if string[0]=="?" else [string[0]]
	for i in range(1,len(string)):
		if string[i]=="?":
			results=results*2
			for idx in xrange(len(results)):
				if (idx<len(results)/2):
					results[idx] +="0"
				else:
					results[idx] +="1"
		else:
			for idx in xrange(len(results)):
				results[idx] +=string[i]

	return results

a="?1?"
print find_comb(a)
