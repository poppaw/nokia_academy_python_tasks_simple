# Create two variables - name and surname - with your own name and surname.
# Then print the string with your data using string joining to get:
# 'Hello. My name is <YOUR_NAME> <YOUR_SOURNAME>. '

preamble = "Hello. My name is"

# put your code here
name_elements = [input("Put your name here: "), input("Put your surname as well: ")]

# 1
print("{} {}.".format(preamble, " ".join(name_elements)))

# 2
print(f"{preamble} {' '.join(name_elements)}.")

# 3
name_elements.insert(0, preamble)
print(" ".join(name_elements) + ".")

