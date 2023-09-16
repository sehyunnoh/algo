# def generate_permutations(elements, perm=[]):
#     if len(elements) == 0:
#         yield perm
#     else:
#         for i in range(len(elements)):
#             new_elements = elements[:i] + elements[i+1:]
#             new_perm = perm + [elements[i]]
#             yield from generate_permutations(new_elements, new_perm)

# # Define a list of elements
# elements = ['a', 'b', 'c']

# # Generate and print permutations
# for perm in generate_permutations(elements):
#     print(perm)

def gen_permutations(arr, n):
    result = []

    if n == 0:
        return [[]]
    for i, elem in enumerate(arr): 
        for P in gen_permutations(arr[:i] + arr[i+1:], n-1):
            result += [[elem]+P]
    return result
    
print(gen_permutations([0, 1, 2], 3))