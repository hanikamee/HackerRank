"""
HackerRank: Leap Year
Difficulty: Easy

Problem: Determine if a year is a leap year using Gregorian calendar rules.

Rules:
1. If divisible by 4 → leap year
2. UNLESS divisible by 100 → not a leap year
3. UNLESS ALSO divisible by 400 → leap year

Examples:
- 1996: divisible by 4, not by 100 → leap year
- 1900: divisible by 4 and 100, not by 400 → not leap year
- 2000: divisible by 4, 100, and 400 → leap year

Input: Integer year (1900 ≤ year ≤ 10^5)
Output: Boolean (True if leap year, False otherwise)
"""


def is_leap(year: int) -> bool:
    """
    Check if a year is a leap year.

    Args:
        year: The year to check

    Returns:
        True if leap year, False otherwise

    Algorithm:
        A year is a leap year if:
        - Divisible by 4 AND (NOT divisible by 100 OR divisible by 400)

    Time Complexity: O(1) - constant number of operations
    Space Complexity: O(1) - fixed variables regardless of input
    """
    leap = False

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True

    return leap


if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
