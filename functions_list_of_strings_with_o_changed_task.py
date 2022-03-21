# Create a function, which takes list of strings and exchanges any letter "o" into "."
# - Check this function on file three_rings.txt.

# put your code here

def change_o_to_dot(original_strings_list):
    changed_strings_list = [i.replace("o", ".") for i in original_strings_list]
    return changed_strings_list


with open("three_rings.txt", "r") as text_file:
    string_list = text_file.read().split()

    new_list = change_o_to_dot(string_list)
    print(new_list)


