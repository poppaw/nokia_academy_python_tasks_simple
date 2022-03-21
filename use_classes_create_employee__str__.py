# Copy solution from use_classes_create_employee file.
# Change the class that your previously created in such a way that calling print(empl) will give the same result as
# calling empl.print_info().

class Employee(object):

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return "{}, {}".format(self.name, self.last_name)


# man = Employee("Jan", "Kowalski")
# print(man)
