def generate_permutations(elements, perm=[]):
    if len(elements) == 0:
        yield perm
    else:
        for i in range(len(elements)):
            new_elements = elements[:i] + elements[i+1:]
            new_perm = perm + [elements[i]]
            yield from generate_permutations(new_elements, new_perm)

# Define a list of elements
elements = ['a', 'b', 'c']

# Generate and print permutations
for perm in generate_permutations(elements):
    print(perm)