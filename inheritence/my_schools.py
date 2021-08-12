from school import School


class PrimarySchool(School):

    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "Primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        return f"{super().__repr__()} with a '{self.pickupPolicy}' pickup policy"


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, "High", numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_sportsTeams(self):
        return self.sportsTeams

    def __repr__(self):
        return f"{super().__repr__()}, and is home of the {self.sportsTeams}"
