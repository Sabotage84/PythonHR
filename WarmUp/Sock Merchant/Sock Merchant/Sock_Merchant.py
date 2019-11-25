import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
	sum=0
	l=int(101)
	colors=[0]*l
	
	for x in ar:
	    colors[x]+=1
	
	for y in colors:
		sum+=y//2
		
	return sum

if __name__ == '__main__':
    
	ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]   
	result = sockMerchant(len(ar), ar)
	print(result)
