def strings_xor(str1: str, str2: str) -> str:
    """
    Performs a bitwise XOR operation on two strings of equal length.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The result of the XOR operation as a string.

    Examples:
        >>> strings_xor("101010", "110011")
        '011001'
        >>> strings_xor("010101", "010101")
        '000000'
    """
    result = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
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
