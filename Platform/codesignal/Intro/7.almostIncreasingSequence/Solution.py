def solution(sequence):
  bad = 0
  for i in range(1, len(sequence)):
    if sequence[i] <= sequence[i-1]:
      bad += 1
    if bad > 1:
      return False
    if i >= 2 and i <= len(sequence) - 2 and sequence[i-2] >= sequence[i] and sequence[i-1] >= sequence[i+1]:
      return False
  return True

# print(solution([1, 3, 2, 1]))
print(solution([10, 1, 2, 3, 4, 5]))



