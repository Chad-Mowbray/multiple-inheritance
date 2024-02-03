class Employee:
    def __init__(self, key_card_no):
        self.key_card_no = key_card_no
        
    def show_up(self):
        print("I'm here")


class Technical(Employee):
    def show_up(self):
        Employee.show_up(self)
        print("Show up in a dirty shirt")


class Manager(Employee):
    def __init__(self, key_card_no, department):
        Employee.__init__(self, key_card_no)
        self.department = department

class ProjectManager(Manager):
    pass


class Developer(Technical):
    def __init__(self, key_card_no, languages):
        Employee.__init__(self, key_card_no)
        # super().__init__(key_card_no)
        self.languages = languages


class HeadEngineer(Developer, ProjectManager):
    def __init__(self, key_card_no, languages, department, degree):
        Developer.__init__(self, key_card_no, languages)
        ProjectManager.__init__(self, key_card_no, department)
        self.degree = degree


if __name__ == "__main__":
    m = Manager("asdf", "sales")
    pass
    # e = Employee("asdf")
    # e.show_up()
    # t = Technical("asdf")
    # t.show_up()