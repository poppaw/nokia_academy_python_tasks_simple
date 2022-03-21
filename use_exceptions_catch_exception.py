# Copy solution from use_exceptions_raise_exception file.
# Try to create a new employee with non-string name or surname and catch exception so program won't stop with error.
from use_exceptions_raise_exception import Employee

try:
    kowalski = Employee("Jan", 3)
except TypeError as e:
    print(f"Creating instance of Employee failed because of {e.__class__.__name__}: {e}.")
    print("Unfortunately, you can't hire Mr Kowalski for this job.")