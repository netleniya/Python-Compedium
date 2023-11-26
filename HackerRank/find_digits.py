def digitize(n: int, base=10):
    while n:
        n, d = divmod(n, base)
        yield d


def find_digits(n: int) -> int:
    return sum(1 for i in digitize(n) if i != 0 and n % i == 0)


def main() -> None:
    num = 1012
    d = find_digits(num)
    print(f"{d} of the numbers in {num} are perfect divisors")


if __name__ == "__main__":
    main()
