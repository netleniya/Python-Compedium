import math


def grade_students(grades: list[int]) -> list[int]:
    """Round up a grade in grades if grade is greater than 38, and the difference between the grade and the next multiple of 5 is less than 3

    Args:
        grades (list[int]): list of student's grades

    Returns:
        list[int]: list of grades rounded to the next multiple of 5
    """
    mult = list(map(lambda x: math.ceil(x / 5) * 5, grades))
    scores = [b if (b - a) < 3 and a >= 38 else a for a, b in zip(grades, mult)]
    return scores


def test_grade_students() -> bool:
    assert grade_students([73, 67, 38, 33]) == [75, 67, 40, 33]
    assert grade_students([37, 38]) == [37, 40]


def main() -> None:
    print(grade_students(grades=[73, 67, 38, 33]))


if __name__ == "__main__":
    main()
