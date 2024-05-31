def counting_sort(arr: list[int]) -> list[int]:

    MAX = 100
    result = [0] * MAX

    for num in arr:
        result[num] += 1

    return result


def main() -> None:
    with open("counting_sort_arr.txt", "r") as f:
        arr = [int(x) for x in f.read().split()]

    print(counting_sort(arr=arr))


if __name__ == "__main__":
    main()
