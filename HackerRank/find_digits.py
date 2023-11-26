def digitize(n: int, base=10):
    """
    Generates the digits of a given number in the specified base.

    Args:
        n (int): The number to digitize.
        base (int, optional): The base to use for digitization. Defaults to 10.

    Yields:
        int: The digits of the number in the specified base.
    """
    while n:
        n, d = divmod(n, base)
        yield d


def find_digits(n: int) -> int:
    """
    Returns the count of non-zero digits in the given number.

    Args:
        n (int): The number to find the digits in.

    Returns:
        int: The count of non-zero digits in the number.
    """
    return sum(i != 0 and n % i == 0 for i in digitize(n))


def test_find_digits() -> bool:
    assert find_digits(123456789) == 3
    assert find_digits(114108089) == 3
    assert find_digits(110110015) == 6
    assert find_digits(106108048) == 5


def main() -> None:
    num = 110110015
    d = find_digits(num)
    print(f"{d} of the numbers in {num} are perfect divisors")


if __name__ == "__main__":
    main()
