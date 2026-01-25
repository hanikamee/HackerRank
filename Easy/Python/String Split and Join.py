"""
HackerRank: String Split and Join
Difficulty: Easy

Problem: Split a string on spaces and join with hyphens.
Input: String with space-separated words
Output: Same words joined with hyphens

Time Complexity: O(n) where n is length of string
Space Complexity: O(n) for the split list and result string
"""


def split_and_join(line: str) -> str:
    """
    Replace spaces with hyphens in a string.

    Args:
        line: Space-separated string

    Returns:
        Hyphen-separated string
    """
    return line.replace(" ", "-")


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
