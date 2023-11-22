def lonelyinteger(lst: list[int]) -> int:
    """
    Returns the integer that appears only once in the given list.
    """
    unique = 0
    for num in lst:
        unique ^= num
    return unique


def test_lonelyinteger() -> bool:
    assert lonelyinteger([1, 2, 2, 3, 3, 4, 4]) == 1
    assert lonelyinteger([1, 1, 2, 2, 3, 3, 4]) == 4
    assert lonelyinteger([0, 0, 1, 2, 1]) == 2


def main() -> None:
    print(lonelyinteger([1, 2, 3, 4, 3, 2, 1]))


if __name__ == "__main__":
    main()
