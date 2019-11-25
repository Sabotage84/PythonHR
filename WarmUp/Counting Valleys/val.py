#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

	val=0
	c=0
	for x in s:
		if (x=='U'):
			c+=1
		else:
			if (c==0):
				val+=1
				c-=1
			else:
				c-=1
	return val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
