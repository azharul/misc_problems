#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. 

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True

NOTE: DO NOT USE LOOPS
"""
def make_bricks(small, big, goal):
  # 5*x+y=goal, x<=big, y<=small
	if (5*big+small)<goal:
		return False
	elif (goal-big*5)>0:
		if (goal-big*5)<=small:
			return True
		else:
			return False
	elif (goal-big*5)<0:
		if goal%5<=small:
			return True
		else:
			return False
	elif goal%5==0 and goal//5<=big:
		return True
	elif goal<=small:
		return True
	else:
		return False

print "make_bricks(3, 1, 8)=",make_bricks(3, 1, 8)
print "make_bricks(3, 2, 10)=",make_bricks(3, 2, 10)
print "make_bricks(3, 1, 9)=",make_bricks(3, 1, 9)
print "make_bricks(3, 2, 8)=",make_bricks(3, 2, 8)
print "make_bricks(6, 1, 11)=",make_bricks(6, 1, 11)
print "make_bricks(6, 0, 11)=",make_bricks(6, 0, 11)
print "make_bricks(1, 4, 11)=",make_bricks(1, 4, 11)
print "make_bricks(0, 3, 10)=",make_bricks(0, 3, 10)
print "make_bricks(1, 4, 12)=",make_bricks(1, 4, 12)
print "make_bricks(7, 1, 11)=",make_bricks(7, 1, 11)
print "make_bricks(43, 1, 46)=",make_bricks(43, 1, 46)
print "make_bricks(40, 2, 47)=",make_bricks(40, 2, 47)
print "make_bricks(20, 4, 38)=",make_bricks(20, 4, 38)
print "make_bricks(200, 250, 1000)=",make_bricks(200, 250, 1000)
