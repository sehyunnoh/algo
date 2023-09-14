def generate_permutations(elements):
    n = len(elements)
    c = [0] * n
    yield elements

    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                elements[0], elements[i] = elements[i], elements[0]
            else:
                elements[c[i]], elements[i] = elements[i], elements[c[i]]
            yield elements
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

# Define a list of elements
elements = ['a', 'b', 'c']

# Generate and print permutations
for perm in generate_permutations(elements):
    print(perm)