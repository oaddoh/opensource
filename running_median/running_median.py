#!/bin/python3

import sys
from heapq import heappush, heappop, nlargest, nsmallest

'''
larger_heap: Contains more than 1 more element than smaller heap. 
'''
def balance_heap(larger_heap, smaller_heap):
    val = heappop(larger_heap)
    heappush(smaller_heap, val)
            
def median(smaller_half_heap, larger_half_heap):
    num_smaller_half_heap = len(smaller_half_heap)
    num_larger_half_heap = len(larger_half_heap)
    
    if(num_smaller_half_heap > num_larger_half_heap):
        return nlargest(1, smaller_half_heap)[0]
    elif(num_smaller_half_heap < num_larger_half_heap):
        return nsmallest(1, larger_half_heap)[0]
    else:
        return (float(nlargest(1, smaller_half_heap)[0]) + float(nsmallest(1, larger_half_heap)[0]))/2
            
#number of elements in stream
n = int(input().strip())
a = []

smaller_half_heap = [] #max heap: python does not support this. Use nlargest(1) to extract the max.
larger_half_heap = [] #min heap
a_1 = int(input().strip())
print("%2.1f" % a_1)
a_2 = int(input().strip())
running_median = (float(a_1) + float(a_2))/2
print("%2.1f" % running_median)

if(a_1 < a_2):
    heappush(smaller_half_heap, a_1)
    heappush(larger_half_heap, a_2)
else:
    heappush(larger_half_heap, a_1)
    heappush(smaller_half_heap, a_2)

#start from the 3rd element
for a_i in range(2, n):
    a_t = int(input().strip())
    smaller_half_heap_max = nlargest(1, smaller_half_heap)[0] #max heap root
    larger_half_heap_min = nsmallest(1, larger_half_heap)[0] #min heap root
    if(a_t < smaller_half_heap_max):
        heappush(smaller_half_heap, a_t)
    else:
        heappush(larger_half_heap, a_t)

    num_smaller_half_heap = len(smaller_half_heap)
    num_larger_half_heap = len(larger_half_heap)
    
    #todo: move to balance heap function
    if((num_smaller_half_heap - num_larger_half_heap) > 1):
        balance_heap(smaller_half_heap, larger_half_heap)
    if((num_larger_half_heap - num_smaller_half_heap) > 1):
        balance_heap(larger_half_heap, smaller_half_heap)

    running_median = median(smaller_half_heap, larger_half_heap)    
    print("%2.1f" % running_median)

