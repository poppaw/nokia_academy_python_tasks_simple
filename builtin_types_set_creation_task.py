# Create a list of unique numbers from lists given:

l1 = [1, 2, 3, 4]
l2 = [1, 2, 12, 44]
l3 = [12, 4, 5, 9]

# put your code here
# 1:
list_of_unique_numbers = [el for el in set(l1 + l2 + l3)]

