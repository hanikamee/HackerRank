"""
HackerRank: Itertools Combinations
Difficulty: Easy

Problem: Print all possible combinations of a string, up to size k,
in lexicographic sorted order.

Input: Space-separated string and integer (e.g., "HACK 2")
Output: All combinations from size 1 to k, one per line

Example:
Input: "HACK 2"
Output:
A
C
H
K
AC
AH
AK
CH
CK
HK
"""
from itertools import combinations, chain


def print_permutations(word, num):
    """
    Print all combinations of a string from size 1 to num.

    Args:
        word: Sorted string to generate combinations from
        num: Maximum combination size

    Algorithm:
        Use chain.from_iterable to flatten combinations of all sizes
        (1 to num) into a single iterable, then print each combination.
    Time Complexity: O(n^k) where n is length of word, k is max size
    - Generating combinations is exponential

    Space Complexity: O(1) for iteration (generator-based)
    """

    all_combos = chain.from_iterable(
        combinations(word, size) for size in range(1, num + 1)
    )

    # Print each combination as a string
    for combo in all_combos:
        print("".join(combo))


def main():
    """Parse input and generate combinations."""
    # Parse space-separated input: "HACK 2"
    word, num = input().split()
    num = int(num)

    # Sort word for lexicographic order
    word = sorted(word)

    print_permutations(word, num)


if __name__ == "__main__":
    main()
