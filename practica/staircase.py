def is_staircase(nums) -> list:
    col_length = 0
    staircase = []

    while len(nums) > 0:
        col_length = col_length + 1
        column = []

        for i in range(0, col_length):
            column.append(nums.pop(0))

        # Check if the current column is valid (all elements increasing)
        for j in range(1, len(column)):
            if column[j] <= column[j - 1]:
                return False

        staircase.append(column)

    # Check if the last column is valid (all elements increasing)
    for j in range(1, len(staircase[-1])):
        if staircase[-1][j] <= staircase[-1][j - 1]:
            return False

    # If entire loop completes, return the staircase
    return staircase
