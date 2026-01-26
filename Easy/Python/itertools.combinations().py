# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations, chain


def print_permutations(word, num):

    all_combos = chain.from_iterable(
        combinations(word, size) for size in range(1, num + 1)
    )

    for combo in all_combos:
        print("".join(combo))


def main():
    word, num = input().split()
    num = int(num)
    word = sorted(word)

    print_permutations(word, num)


if __name__ == "__main__":
    main()
