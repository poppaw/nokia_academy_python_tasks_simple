# Copy solution from use_classes_company file.
# Modify Employee class to prevent from providing non-string value as name or last_name by throwing an Exception
# You can use e.g. 'AttributeError'

class Employee(object):

    def __init__(self, name, last_name):
        if type(name) is not str:
            raise TypeError("@name must be str")
        self.name = name
        if type(last_name) is not str:
            raise TypeError("@last_name must be str")
        self.last_name = last_name

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)


# man = Employee("Jan", "Kowalski")
# error_man = Employee(1, "Kowalski")

