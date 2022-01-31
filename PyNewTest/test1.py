#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(18)
    if n % 2 != 0:
        print(n/2)
        print("Weird1")
    else:
        if n >= 2 and n <= 5:
            print("Not Weird2")
        elif 6 <= n <= 20:
            print("Weird3")
        else:
            print("Not Weird4")



