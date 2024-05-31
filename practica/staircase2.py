def is_staircase(nums):
    col_length = 0
    while len(nums) > 0:
        col_length += 1
        if len(nums) < col_length:
            return False
        for _ in range(col_length):
            nums.pop(0)
    return True


# Example usage
# print(is_staircase([1, 2, 3, 4, 5, 6]))  # Should return True
# print(is_staircase([1, 2, 3, 4, 5]))     # Should return False
