def factorial(num: int) -> int:
    if num < 2:
        return 1
    return num * factorial(num - 1)


def main() -> None:
    print(factorial(25))


if __name__ == "__main__":
    main()
