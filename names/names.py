import os, time

from binary_search_tree import BSTNode


def full_path(filename:str) -> str:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, filename)


start_time = time.time()

f = open(full_path('names_1.txt'), 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(full_path('names_2.txt'), 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# create first binary search tree node
bst = BSTNode(names_1[0])
# populate binary search tree with remaining names
for name in names_1[1:]:
    bst.insert(name)

# find duplicates
duplicates = [name for name in names_2 if bst.contains(name)]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# went from > 12 seconds to < 1 second
# runtime: 0.1772751808166504 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

print('\n\n------------------ Stretch -----------------\n\n')

start_time = time.time()

f = open(full_path('names_1.txt'), 'r')
names_1 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

f = open(full_path('names_2.txt'), 'r')
names_2 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

duplicates = list(names_1.intersection(names_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# runtime: 0.006196260452270508 seconds
