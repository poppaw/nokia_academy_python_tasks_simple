# Create a function calculating sum for any number of integers given to that function
# as arguments

# put your code here
def calculate(*args):
    return sum(args)


test_calculate = calculate(1, 2, 5, 6, 7)
print(f"args = 1,2,5,6,7: {test_calculate}")

test_calculate_1 = calculate(*range(1, 9)) # typeError without *
print(f"args = *range(1,9): {test_calculate_1}")


