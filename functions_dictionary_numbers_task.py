# You have two lists, both randomly ordered: list of integers and list of string integers.
# Create a dictionary with numbers that match: {1: '1', 3: '3', 10: '10'}


integers = [3, 1, 4, 6, 10]
strings = ['1', '5', '10', '3']


# **************
# Using 'for' loop:
# **************

# place your code here
integers.sort()
# 1
dictionary = {}
for i in integers:
    if str(i) in strings:
        dictionary[i] = str(i)
print(dictionary)
print("done")

# 2
dictionary2 = {i: str(i) for i in integers if str(i) in strings}
print(dictionary2)

assert dictionary == dictionary2









# **************
# Using dict comprehension:
# **************

# place your code here



