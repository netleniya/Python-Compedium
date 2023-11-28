def count_substring(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in a string.

    Args:
        string (str): The string to search for occurrences of the substring.
        substring (str): The substring to count occurrences of.

    Returns:
        int: The number of occurrences of the substring in the string.
    """
    return sum(string[i:].startswith(substring) for i in range(len(string)))


def main() -> None:
    print(count_substring("ininini", "ini"))


if __name__ == "__main__":
    main()
