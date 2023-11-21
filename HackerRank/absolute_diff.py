def minimum_absolute_difference(arr: list[int]) -> int:
    """
    Calculate the minimum absolute difference between any two elements in the given list.

    Args:
        arr (list[int]): A list of integers.

    Returns:
        int: The minimum absolute difference between any two elements in the list."""

    minimum = float("inf")
    arr.sort()

    for i in range(len(arr)):
        diff = abs(arr[i - 1] - arr[i])
        minimum = min(minimum, diff)
    return minimum


def test_minimum_absolute_difference() -> bool:
    """
    Test the minimum_absolute_difference function.

    Returns:
        bool: True if all the test cases pass, False otherwise."""

    assert (
        minimum_absolute_difference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]) == 1
    )
    assert minimum_absolute_difference([1, -3, 71, 68, 17]) == 3


def main() -> None:
    print(minimum_absolute_difference([1, -3, 71, 68, 17]))


if __name__ == "__main__":
    main()
