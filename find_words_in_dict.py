#!/usr/bin/python
#Problem on matching a string to words in a dictionary

# the following function will return the corresponding keys of dictionary that matches string items
def match_words(string,dictionary):
	for key,word in dictionary.items():
		if word in string:
			#key=[key for key,value in D.iteritems() if value==word]
			print str(word)+" is found at "+str(key)


D={1:"ronaldo",2:"messi",3:"neymar",4:"martial",5:"reus",6:"hazard",7:"alexis"}
S="Although ronaldo and messi have been dominating european football for the past 8-9 years, players like neymar, reus, hazard etc have made their mark"
match_words(S,D)
