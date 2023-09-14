from itertools import permutations

# Define a list of elements
elements = ['a', 'b', 'c']

# Generate all permutations of the list
permutations_list = permutations(elements)

# Convert the permutations to a list (if needed)
permutations_list = list(permutations_list)

# Print the permutations
for perm in permutations_list:
    print(perm)
