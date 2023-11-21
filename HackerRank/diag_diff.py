def diagonal_difference(arr: list[[int]]) -> int:
    d1, d2 = 0, 0
    n = len(arr)
    for i in range(n):
        d1 += arr[i][i]
        d2 += arr[i][n - 1 - i]
    return abs(d1 - d2)


def test_diagonal_difference() -> bool:
    ...


if __name__ == "__main__":
    matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    print(diagonal_difference(arr=matrix))
