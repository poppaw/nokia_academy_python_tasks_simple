# Copy solution from use_exceptions_catch_exception file.
# Create your own Exception class to handle the problem in 1st exercise with exceptions.
# Change previously used Exception 'AttributeError' to the one that your created.


class WrongPersonChoosenException(ValueError):
    def __init__(self, value):
        self.wrong_value = value
        self.correct_value = "Kowalski"

    def __str__(self):
        return f'{self.wrong_value} is given but {self.correct_value} is expected for this position.'


class Employee(object):

    def __init__(self, name, last_name):
        if type(name) is not str:
            raise TypeError("@name must be str")
        self.name = name
        if last_name != "Kowalski":
            raise WrongPersonChoosenException(last_name)
        self.last_name = last_name

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)


nowak = Employee("Jan", "Nowak")