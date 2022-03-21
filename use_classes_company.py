# Copy solution from use_classes_create_employee_inheritance file.
# Create class Company which takes LIST of employees as a parameter upon object creation.
# Print on instance of such class should display list of all employees.
# Test if on a list created from following employees:
# Guido van Rossum - programmer
# Roman Mr.Bean - programmer
# Steve Jobs - manager
# Output should be following:
#   Guido, van Rossum, programmer
#   Roman, Mr.Bean, programmer
#   Steve, Jobs, manager

from use_classes_create_employee_inheritance import Programmer, Manager


class Company(object):
    def __init__(self, employees):
        self.__employees = employees

    def __str__(self):
        return "\n".join(["{}".format(i) for i in self.__employees])

    def append(self, employee):
        self.__employees.append(employee)


nokia = Company([])
print(f"Step #1 \n{nokia}")

rossum = Programmer("Guido", "van Rossum")
bean = Programmer("Roman", "Mr.Bean")
jobs = Manager("Steve", "Jobs")
zelent = Programmer("Mirosław", "Zelent")

nokia._Company__employees = [rossum, bean]
print(f"Step #2 \n{nokia}")

nokia._Company__employees.append(jobs)
print(f"Step #3 \n{nokia}")

nokia.append(zelent)
print(f"Step #4 \n{nokia}")




