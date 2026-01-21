"""
HackerRank: Capitalize (Passport Names)
Difficulty: Easy

Problem: Capitalize the first letter of each word in a name while preserving
all original spacing (including multiple spaces).

Rules:
- First letter of each word should be capitalized
- Rest of the characters remain unchanged
- All spacing (single, multiple, leading, trailing) must be preserved exactly
- Numbers and special characters remain as-is

Input: String containing full name with alphanumeric characters and spaces
Output: String with first letter of each word capitalized

Examples:
- "chris alan" → "Chris Alan"
- "chris  alan" → "Chris  Alan" (double space preserved)
- "12abc def" → "12abc Def" (numbers stay as-is)
"""


def solve(passport_name: str) -> str:
    """
    Capitalize the first character of each word while preserving spacing.

    Args:
        passport_name: The full name string to capitalize

    Returns:
        String with first letter of each word capitalized

    Algorithm:
        Iterate through each character with its index.
        If the character is at position 0 OR the previous character is a space,
        it's the start of a word, so capitalize it.
        Otherwise, keep the character as-is.
        This preserves all original spacing.

    Time Complexity: O(n) where n is the length of the string
        - Single pass through all characters
        - Constant time operations per character

    Space Complexity: O(n)
        - Result list grows linearly with input size
        - Final string is also O(n)
    """
    capitalized_name: list = []

    for i, char in enumerate(passport_name):
        # Check if this is the start of a word
        if i == 0 or passport_name[i - 1] == ' ':
            capitalized_name.append(char.upper())

        else:
            capitalized_name.append(char)

    return "".join(capitalized_name)


if __name__ == '__main__':

    name = input("Enter the passport name: ")
    result = solve(name)
    print(result)
