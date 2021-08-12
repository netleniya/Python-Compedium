class School:

    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    @property
    def get_numberOfStudents(self):
        return self.numberOfStudents

    @get_numberOfStudents.setter
    def set_numberOfStudents(self, students):
        self.numberOfStudents = students

    def __repr__(self):
        return f"{self.name} is a {self.level} school with {self.numberOfStudents} pupils"
