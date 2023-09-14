def solution(n):
  return sum([int(x) for x in str(n) if int(x) % 2]) == 0

def solution(n):
  return all([int(x)%2==0 for x in str(n)])

print(solution(248622))