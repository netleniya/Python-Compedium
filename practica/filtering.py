import random
from timeit import repeat


def main() -> None:
    lst: list[int] = [random.randint(1, 1000) for _ in range(1000)]

    t0: float = min(
        repeat(
            "[x for x in lst if not x %2]",
            globals={"lst": lst},
            number=100_000,
            repeat=2,
        )
    )

    print(f"Elapsed : {t0:.3f}s")


if __name__ == "__main__":
    main()
