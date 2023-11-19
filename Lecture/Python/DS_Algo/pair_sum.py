def pair_sum(myList, sum):
  result = []
  for i, x in enumerate(myList):
    arr = myList[i+1:]
    if sum - x in arr:
      result.append(f'{x}+{sum-x}')
  return result
    

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))