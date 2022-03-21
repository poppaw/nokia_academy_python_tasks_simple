# Create a list of squares of first 10 integers:
# [1, 4, 9, ..., 100]

# **************
# Using 'for' loop:
# **************

# place your code here
# 1
square_list = []
for i in range(1, 11):
    square_list.append(i ** 2)
    print(square_list)

# 2
another_square_list = [i ** 2 for i in range(1, 11)]
print(another_square_list)

print(square_list == another_square_list)







# **************
# Using built-in 'map':
# **************

# place your code here







# **************
# Using list comprehension:
# **************

# place your code here







