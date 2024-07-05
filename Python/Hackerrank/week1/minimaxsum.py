#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # minelm = min(arr)
    # maxelm = max(arr)
    # minarr = sum(arr) - maxelm
    # maxarr = sum(arr) - minelm
    # print(f'{minarr} {maxarr}')
    arr.sort()
    min = sum(arr[:-1])
    max = sum(arr[1:])
    print(f'{min} {max}')

    

if __name__ == '__main__':
    print("Enter a list of numbers separated by spaces:")
    #when prompted write a series of numbers on same line seperated by space

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
