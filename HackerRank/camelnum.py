def camel_case(in_str: str) -> int:
    return 1 + sum(1 for c in in_str if c.isupper())


def test_camel_case() -> bool:
    assert camel_case("saveChangesInTheEditor") == 5


def main() -> None:
    ...


if __name__ == "__main__":
    main()
