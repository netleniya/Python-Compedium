def pairs(k, arr):
    """
    Counts the number of pairs in the given list with a difference of k.

    This function takes an integer k and a list arr as input.
    It returns the count of pairs of elements in arr whose difference is equal to k.

    Args:
        k (int): The desired difference between pairs.
        arr (list): The list of integers to search for pairs.

    Returns:
        int: The count of pairs with a difference of k.
    """
    arr_set = set(arr)
    return sum(a - k in arr_set for a in arr)


def test_pairs() -> bool:
    assert (
        pairs(
            1,
            [
                363374326,
                364147530,
                61825163,
                1073065718,
                1281246024,
                1399469912,
                428047635,
                491595254,
                879792181,
                1069262793,
            ],
        )
        == 0
    )
    assert pairs(2, [1, 3, 5, 8, 6, 4, 2]) == 5


def main() -> None:
    print(pairs(2, [1, 5, 3, 4, 2]))


if __name__ == "__main__":
    main()
