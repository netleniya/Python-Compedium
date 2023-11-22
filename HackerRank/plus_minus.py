def plus_minus(arr: list[int]) -> tuple[float]:
    pos = round(sum(map(lambda x: x > 0, arr)) / len(arr), 6)
    neg = round(sum(map(lambda x: x < 0, arr)) / len(arr), 6)
    zer = round(sum(map(lambda x: x == 0, arr)) / len(arr), 6)

    return pos, neg, zer


def test_plus_minus() -> bool:
    assert plus_minus([-4, 3, -9, 0, 4, 1]) == (0.500000, 0.333333, 0.166667)
    assert plus_minus([1, 2, 3, -1, -2, -3, 0, 0]) == (0.375000, 0.375000, 0.250000)


def main() -> None:
    print(plus_minus([-4, 3, -9, 0, 4, 1]))


if __name__ == "__main__":
    main()
