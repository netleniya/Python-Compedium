def findZigZagSequence(a):
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
