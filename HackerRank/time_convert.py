def convert_time(string: str) -> str:
    """Given a time in 12-hour AM/PM format, convert it to 24-hour time

    Args:
        string (str): time in 12-hour format

    Returns:
        str: 12 in 24-hour format
    """
    hour = int(string.split(":")[0])

    if string.endswith("PM"):
        hour += 12
        if hour > 23:
            hour = "12"
    elif string.endswith("AM"):
        if hour == 12:
            hour = "00"
        else:
            hour = str(hour).zfill(2)

    return string.replace(string[:2], str(hour))[:-2]


def test_convert_time() -> bool:
    assert convert_time("07:05:45PM") == "19:05:45"
    assert convert_time("02:40:22AM") == "02:40:22"
    assert convert_time("12:40:22AM") == "00:40:22"
    assert convert_time("11:59:59PM") == "23:59:59"


def main():
    print(case1 := convert_time("07:05:45PM"))


if __name__ == "__main__":
    main()
