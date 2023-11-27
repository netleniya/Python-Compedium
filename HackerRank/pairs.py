def pairs(k, arr):
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
