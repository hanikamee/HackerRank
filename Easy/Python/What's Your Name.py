"""
HackerRank: What's Your Name?
Difficulty: Easy

Problem: Given first and last name, print a greeting message.
Input: Two lines - first name, then last name
Output: "Hello {first} {last}! You just delved into python."
"""


def print_full_name(first: str, last: str) -> None:
    """
    Print a greeting with the person's full name.

    Args:
        first: First name
        last: Last name

    Time Complexity: O(1) - constant operations
    Space Complexity: O(1) - fixed string creation
    """
    result = f"Hello {first} {last}! You just delved into python."
    print(result)


if __name__ == "__main__":
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
