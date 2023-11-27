def camel_case(in_str: str) -> int:
    """
    Counts the number of uppercase letters in a given string.

    This function takes a string in_str as input and returns the count of uppercase letters in the string.

    Args:
        in_str (str): The input string to count uppercase letters from.

    Returns:
        int: The count of uppercase letters in the input string.
    """
    return 1 + sum(c.isupper() for c in in_str)


def test_camel_case() -> bool:
    assert camel_case("saveChangesInTheEditor") == 5


def main() -> None:
    ...


if __name__ == "__main__":
    main()
