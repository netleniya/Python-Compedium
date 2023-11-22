def diagonal_difference(arr: list[[int]]) -> int:
    """
    Calculates the absolute difference between the sums of the primary and secondary diagonals of a square matrix.

    Explanation:
    - The function takes a square matrix as input.
    - It calculates the sum of the elements on the primary diagonal and the sum of the elements on the secondary diagonal.
    - The function returns the absolute difference between the two sums.

    Args:
    - arr (list[list[int]]): A square matrix represented as a list of lists of integers.

    Returns:
    - int: The absolute difference between the sums of the primary and secondary diagonals of the matrix.
    """

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
