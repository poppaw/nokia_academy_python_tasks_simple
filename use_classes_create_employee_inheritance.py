# Copy solution from use_classes_create_employee__str__ file.
# Create classes Programmer and Manager derived from Employee. Calling print on such class object should add <position>
# into description built in previous exercise. Consider using super().
# Final string should look like this: '<name>, <last_name>, <position>'
from use_classes_create_employee__str__ import Employee


class Programmer(Employee):

    def __init__(self, name, last_name):
        # super(Programmer, self).__init__(name, last_name) # works for both 2 and 3 Python
        Employee.__init__(self, name, last_name) # works only for python3
        self.position = "programmer"

    def __str__(self):
        # works for python 2 and 3
        # return super(Programmer, self).__str__() + ", {}".format(self.position)
        # works for python3:
        return super().__str__() + ", {}".format(self.position)

class Manager(Employee):

    def __init__(self, name, last_name):
        super(Manager, self).__init__(name, last_name) # works for both 2 and 3 Python
        # Employee.__init__(self, name, last_name) # works only for python3
        self.position = "manager"

    def __str__(self):
        # works for python 2 and 3
        return super(Manager, self).__str__() + ", {}".format(self.position)
        # works for python3:
        # return super().__str__() + ", {}".format(self.position)


kowalski = Programmer("Jan", "Kowalski")
nowak = Manager("Józef", "Nowak")
# print(kowalski)
# print(nowak)


