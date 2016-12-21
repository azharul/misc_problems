#!/usr/bin/python

#Write Interleaving Iterator class which takes a list of Iterators as input and iterates one element at a time from each iterator until they are all empty
# interleaving iterators are also called Round Robin iterator

from itertools import islice, cycle
 
def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    pending = len(iterables)
    nexts = cycle(iter(it).next for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))

print list(roundrobin(range(5),"hello")
