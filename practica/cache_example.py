from functools import cache
from timeit import timeit


@cache
def factorial(n: int) -> int:
    return n * factorial(n - 1) if n else 1


@cache
def fibonacci(n: int) -> int:
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else n


def main() -> None:
    t0: float = timeit("f(10)", globals={"f": factorial})
    t1: float = timeit("f(5)", globals={"f": factorial})
    t2: float = timeit("f(12)", globals={"f": factorial})

    t3: float = timeit("f(40)", globals={"f": fibonacci})

    print(
        f"""
        Factorial1 : {t0:.3f}
        Factorial2 : {t1:.3f}
        Factorial3 : {t2:.3f}

        Fibonacci : {t3:.3f}
"""
    )


if __name__ == "__main__":
    main()
