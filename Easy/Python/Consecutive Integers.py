"""
HackerRank: Print Consecutive Integers
Difficulty: Easy

Problem: Print consecutive integers from 1 to n as a single string.
Input: Integer n (1 ≤ n ≤ 150)
Output: String of consecutive numbers without spaces (e.g., "123" for n=3)
"""


def print_list(number: int) -> str:
    """
    Generate a string of consecutive integers from 1 to number.
    
    Args:
        number: Upper bound (inclusive)
    
    Returns:
        String containing consecutive integers without spaces
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return ''.join(str(num) for num in range(1, number + 1))

if __name__ == '__main__':
    number = int(input())
    print(print_list(number))
    
