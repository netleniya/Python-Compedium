def diagonal_difference(arr: list[[int]]) -> int:
    n = len(arr)
    d1 = sum(arr[i][i] for i in range(n))
    d2 = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(d1 - d2)


def test_diagonal_difference() -> bool:
    assert diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]) == 15
    assert diagonal_difference([[6, 8], [-6, 9]]) == 13


if __name__ == "__main__":
    matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    print(diagonal_difference(arr=matrix))
