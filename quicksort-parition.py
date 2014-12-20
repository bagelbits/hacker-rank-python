#!/bin/python
def partition(ar):    
    p = ar[0]
    smaller = []
    larger = []
    for x in ar:
        if x == p:
            continue
        elif x < p:
            smaller.append(x)
        else:
            larger.append(x)
    smaller.append(p)
    smaller.extend(larger)
    print " ".join(smaller)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)