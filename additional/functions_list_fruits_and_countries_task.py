# You have two lists: list of fruits and list of countries.
# Create a third list, containing pairs (tuples) of fruits and countries that start with same letter:

# place your code here

fruits = ['cherry', 'apple', 'melon', 'grape', 'pomelo', 'strawberry']
countries = ['vietnam', 'poland', 'sweden', 'india', 'canada', 'finland', 'denmark']

# **************
# Using 'for' loop:
pairs_list = []
# first_letter_index = 0
for fr in fruits:
    for country in countries:
        if country.startswith(fr[0]):
            pairs_list.append((fr, country))
print(pairs_list)


# **************
# Using list comprehension:
pairs_list_v2 = [(fr, country) for fr in fruits for country in countries if country.startswith(fr[0])]
print(pairs_list_v2)
assert pairs_list == pairs_list_v2
