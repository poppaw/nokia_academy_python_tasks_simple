# Write a program that prints sorted list of words from three_rings.txt
# 
# words should be unique (ignore case-sensitive)
# words should not have any dots
# words should not have any commas

# put your code here

with open("../three_rings.txt", "r") as text_file:
    string_list = text_file.read().split()
    flatten_list = [el.casefold().rstrip(",").rstrip(".") for el in string_list]
    flatten_set = set(flatten_list)
    finally_list = list(flatten_set)
    finally_list.sort()

    # print(string_list)
    # print(flatten_list)
    # print(flatten_set)
    print(finally_list)

