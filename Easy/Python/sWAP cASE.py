"""
HackerRank: Swap Case
Difficulty: Easy

Problem: Swap the case of all letters in a string.
Lowercase → Uppercase, Uppercase → Lowercase, Others unchanged.

Input: String with mixed characters
Output: String with swapped cases

Example: "HackerRank.com" → "hACKERrANK.COM"
"""


def swap_case(string: str) -> str:
    """
    Swap case of all alphabetic characters in string.

    Args:
        string: Input string with mixed characters

    Returns:
        String with cases swapped

    Time Complexity: O(n) - iterate through each character once
    Space Complexity: O(n) - build result string of same length
    """
    result = ""
    for letter in string:
        result += letter.capitalize() if letter.islower() else letter.lower()

    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
