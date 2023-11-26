from functools import cache


@cache
def factorial(num: int) -> int:
    """
    Calculates the factorial of a given number.

    Args:
        num (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the given number.

    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
    """
    return 1 if num < 2 else num * factorial(num - 1)


def main() -> None:
    print(factorial(25))


if __name__ == "__main__":
    main()
