#!/bin/python3

""" 
HackerRank: Python If-Else
Difficulty: Easy
Problem: Determine if a number is "Weird" based on specific conditional rules.
- Odd numbers are always weird
- Even numbers in range 2-5 are not weird
- Even numbers in range 6-20 are weird
- Even numbers greater than 20 are not weird

Input: A single positive integer n (1 ≤ n ≤ 100)
Output: Print "Weird" or "Not Weird"
"""


import math
import os
import random
import re
import sys

def print_number(number):
    """  
    Classify and print whether a number is weird or not weird.
    The function evaluates the number against specific rules:
    odd numbers are always weird, while even numbers are weird
    only if they fall within the range 6-20.
    
    
    Time Complexity: O(1)
    Time Complexity: O(1)
    """
    odd = number % 2 == 1 
    weird_range = not odd and 6 <= number <= 20
    
    if odd or weird_range:
        print("Weird")
    else:
        print("Not Weird")    
    
        

if __name__ == '__main__':
    number = int(input().strip())
    print_number(number)
