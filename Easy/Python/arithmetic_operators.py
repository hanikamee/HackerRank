"""
HackerRank: Arithmetic Operations
Difficulty: Easy

Problem: Given two integers, perform addition, subtraction, and multiplication.
Input: Two integers on separate lines
Output: Three integers on separate lines (sum, difference, product)
"""


def compute(first_number: int, second_number: int) -> tuple[int, int, int]:
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        first_number: The first operand
        second_number: The second operand
    
    Returns:
        A tuple containing (sum, difference, product)
    
    Time Complexity: O(1)
    Space Complexity: O(1)    
    """
    addition: int = first_number + second_number
    subtraction: int = first_number- second_number
    multiplication: int = first_number * second_number
    
    return addition, subtraction, multiplication  

if __name__ == '__main__':
    first_number = int(input())
    second_number = int(input())
    
    # Compute and print results, each on a new line
    print (*compute(first_number, second_number), sep = '\n')
    