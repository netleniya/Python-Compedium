from school import School
from my_schools import HighSchool, PrimarySchool


def main():
    '''Test cases for creating Highschools and Primary Schools from Classes'''

    # Create a Primary school object and print
    dom = PrimarySchool("Westdale", 400, "3:15pm onwards")
    print(dom.__repr__())

    # Change the number of students
    dom.set_numberOfStudents = 310
    print(dom.__repr__())

    # Create a High school object and print
    mag = HighSchool("Magellan", 2495, "Spherical Chickens")
    print(mag.__repr__())


if __name__ == "__main__":
    main()
