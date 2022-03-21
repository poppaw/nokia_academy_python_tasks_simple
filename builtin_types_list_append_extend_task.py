# Create a list as presented using only append and extend and the items given below:
# [[1], ['a'], [(1,3,4), 's'], "Alice doesn't have a cat", 'has a mirror']


a = [1]
b = []
c = "a"
d = [(1, 3, 4)]
e = 's'
f = "Alice doesn't have a cat"
g = "has a mirror"

final_list = []

# place your code here

final_list.append(a)
final_list.append([c])
d.append(e)
final_list.append(d)
final_list.append(f)
final_list.append(g)
print(final_list)
