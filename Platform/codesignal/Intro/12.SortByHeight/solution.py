def solution(a):
  people = sorted([x for x in a if x != -1])
  return [people.pop(0) if x != -1 else -1 for x in a ]


print(solution([-1, 150, 190, 170, -1, -1, 160, 180]))