#!/usr/bin/env python3


def revert(s: str) -> str:
    """
    Note: this could easily be done with s[::-1], but to show the algorithm
    working it will be done manually.
    """
    length: int = len(s)
    characters = []
    for i in range(length):
        characters.append(s[-(i + 1)])
    return "".join(characters)


def main():
    entry_str: str = input("String a ser invertida > ")
    print(f"Revertido: '{revert(entry_str)}'")


if __name__ == "__main__":
    main()
