"""
HackerRank: Division
Difficulty: Easy

Problem: Perform integer and float division on two numbers.
Input: Two integers a and b
Output: Two lines - integer division result, then float division result


Time Complexity: O(1)
Space Complexity: O(1)
"""


def divide(first_number, second_number) -> tuple[int, float]:
    integer_number: int = first_number // second_number
    float_number: float = first_number / second_number

    return integer_number, float_number


if __name__ == '__main__':
    first_number = int(input())
    second_number = int(input())
    print(*divide(first_number, second_number), sep='\n')
