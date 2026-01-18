"""
HackerRank: Squares of Numbers
Difficulty: Easy

Problem: For a given integer n, print the square of all non-negative 
integers less than n (i.e., 0 to n-1).

Input: Single integer n (0 ≤ n ≤ 20)
Output: n lines, each containing the square of the corresponding index
"""

def square_number(number: int) -> list [int]:
    """ 
    Generate squares of all numbers from 0 to number-1.
    """
    
    squared_list = []
    for num in range(number):
        squared_list.append(num ** 2)
    return squared_list    

if __name__ == '__main__':
    number: int = int(input())
    print(*square_number(number), sep = '\n')