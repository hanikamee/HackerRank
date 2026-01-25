"""
HackerRank: Text Wrap
Difficulty: Easy

Problem: Wrap a string into multiple lines of specified width.
Input: String and max width integer
Output: String with newline characters at wrap points

Example: "ABCDEFGH", width=4 → "ABCD \n EFGH"
"""


def wrap(string, max_width):
    """
    Wrap string into lines of maximum width.

    Args:
        string: String to wrap
        max_width: Maximum characters per line

    Returns:
        Wrapped string with newline separators

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return "\n".join(
        string[i: i + max_width] for i in range(0, len(string), max_width)
    )


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
