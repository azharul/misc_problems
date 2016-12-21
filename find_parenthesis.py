#!/usr/bin/python

#Write a function if a given string has a balanced parenthesis,bracket,curly bracket

# the following function can find balanced parenthesis, assuming the string always HAVE the parenthesis
def find_paren(string):
	paren1=0
	paren2=0
	start=False
	stop=False
	for i in string:
		if i=="[":
			start=True
			stop=False
		elif i=="]" and start==True:
			stop=True
			start=False

	if "[" in string and stop==True:
		print "balanced parenthesis"
	elif "[" not in string and stop==False:
		print "balanced parenthesis"
	else:
		print "Unbalanced parenthesis"
# same code for bracket and curly bracket
	
	

S="12a-3b[4a^2-2c{8c-4b^2(3a-2c)+2ab(5b-3c)}-5ac][]+3bc"
find_paren(S)
