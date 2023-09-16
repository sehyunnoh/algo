from itertools import permutations

def solution(a):
  for arr in list(permutations(a)):
    all_true = False
    for i in range(len(arr) - 1):
      if len([j for j in range(len(arr[i])) if arr[i][j] != arr[i+1][j]]) == 1:
        all_true = True
      else:
        all_true = False
        break
    if all_true:
      return True
  return False


def diff(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1

def solution2(inputArray):
    for z in permutations(inputArray):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
            return True
    return False

# print(solution(["aba", "bbb", "bab"])) // False
print(solution(["abc",  "abx",  "axx",  "abx",  "abc"])) # True
# print(solution(["abc",  "bef",  "bcc",  "bec",  "bbc",  "bdc"])) # True