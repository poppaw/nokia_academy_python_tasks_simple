# Create a function, which takes strings list and returns only those strings which start from letter "b".
# - Check this function on file three_rings.txt.


# put your code here
# 1
def select_words(string_list):
    # f = lambda w: w.startswith("b")
    return list(filter(lambda x: x.startswith("b"), string_list))


# 2
def select_words_v_2(string_list):
    return [el for el in string_list if el.startswith("b")]


with open("three_rings.txt", "r") as text_file:
    words_list = text_file.read().split()

    new_list = select_words(words_list)
    print(new_list)

    another_new_list = select_words_v_2(words_list)
    print(another_new_list)

    assert new_list == another_new_list


