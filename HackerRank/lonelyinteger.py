def lonelyinteger(lst: list[int]) -> int:
    """
    Returns the integer that appears only once in the given list.

    Explanation:
    - The function takes a list of integers as input.
    - It finds the integer that appears only once in the list.
    - The function returns the unique integer.

    Args:
    - lst (list[int]): A list of integers.

    Returns:
    - int: The integer that appears only once in the list.

    Examples:
    >>> lonelyinteger([1, 2, 2, 3, 3, 4, 4])
    1
    >>> lonelyinteger([1, 1, 2, 2, 3, 3, 4])
    4"""

    nums = {}
    for key in lst:
        if key not in nums:
            nums[key] = 1
        else:
            nums[key] += 1

    for key, val in nums.items():
        if val == 1:
            return key


def test_lonelyinteger() -> bool:
    assert lonelyinteger([1, 2, 2, 3, 3, 4, 4]) == 1
    assert lonelyinteger([1, 1, 2, 2, 3, 3, 4]) == 4
    assert lonelyinteger([0, 0, 1, 2, 1]) == 2


def main() -> None:
    print(lonelyinteger([1, 2, 3, 4, 3, 2, 1]))


if __name__ == "__main__":
    main()
