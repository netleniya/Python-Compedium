def findZigZagSequence(a: list[int]) -> None:
    """
    Modifies the input list to create a zigzag sequence and prints the elements.

    This function takes a list 'a' as input and modifies it in-place to create a zigzag sequence.
    The zigzag sequence is created by sorting the list, swapping the middle element with the last element,
    and then performing a swapping operation between elements from the middle index + 1 to the second-to-last index.
    Finally, it prints the elements of the modified list.

    Args:
        a (list): The list of elements to be modified.

    Returns:
        None
    """
    a.sort()
    mid = len(a) // 2
    a[mid], a[-1] = a[-1], a[mid]

    st = mid + 1
    ed = len(a) - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st += 1
        ed -= 1

    print(*a)


def main():
    findZigZagSequence([1, 2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
    main()
