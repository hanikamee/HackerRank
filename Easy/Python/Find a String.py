"""
HackerRank: Find a String (Count Substring Occurrences)
Difficulty: Easy

Problem: Count how many times a substring occurs in a string.
String traversal is left to right, case-sensitive.

Input: 
- Line 1: Original string
- Line 2: Substring to search for

Output: Integer count of occurrences

Example:
Input: "ABCDCDC", "CDC"
Output: 2 (found at positions 2 and 4)
"""


def count_substring(string: str, sub_string: str) -> int:
    """
    Count occurrences of sub_string in string.

    Args:
        string: The text to search in
        sub_string: The pattern to search for

    Returns:
        Number of times sub_string appears in string

    Algorithm:
        Loop through each valid starting position in the string.
        At each position, extract a slice of length len(sub_string).
        Compare the slice to sub_string. If match, increment counter.

    Time Complexity: O(n × m) where n = len(string), m = len(sub_string)
    Space Complexity: O(1) - only using counter and loop variables
    """

    count: int = 0
    for character in range(len(string) - len(sub_string) + 1):
        if string[character: character+len(sub_string)] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
