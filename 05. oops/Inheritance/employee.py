# Base class
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_role_description(self):
        return "Employee role"


# Child class: Developer
class Developer(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)

    def get_role_description(self):
        return "Software Developer writes code for applications"


# Child class: Tester
class Tester(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)

    def get_role_description(self):
        return "tester tests the applications for bugs"


# Child class: Manager
class Manager(Employee):
    def __init__(self, id, name):
        super().__init__(id, name)

    def get_role_description(self):
        return "manager manages the team and project"


# Main execution
if __name__ == "__main__":

    e1 = Developer(1, "Jadeja Mouryrajsinh")
    print(f"{e1.name}: {e1.get_role_description()}")

    e2 = Tester(2, "Zala")
    print(f"{e2.name}: {e2.get_role_description()}")

    e3 = Manager(3, "Kushagra")
    print(f"{e3.name}: {e3.get_role_description()}")
