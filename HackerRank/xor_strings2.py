def strings_xor(str1: str, str2: str) -> str:
    result: str = ""
    for idx in range(len(str1)):
        if str1[idx] == str2[idx]:
            result += "0"
        else:
            result += "1"

    return result


def main() -> None:
    s1 = "10101"
    s2 = "00101"
    print(strings_xor(str1=s1, str2=s2))


if __name__ == "__main__":
    main()
