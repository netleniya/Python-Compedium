def digitize(n: int, base=10):
    while n:
        n, d = divmod(n, base)
        yield d


def find_digits(n: int) -> int:
    return sum(not n % i for i in list(digitize(n)) if i != 0)
