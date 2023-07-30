def solution(a):
  result = [0, 0]
  for i, x in enumerate(a):
    if i%2 == 0:
      result[0] += x
    else:
      result[1] += x
  return result

def solution2(a):
  result = [0,0]
  for i, x in enumerate(a):
    result[i%2] += x
  return result


def solution3(a):
  return [sum(a[::2]), sum(a[1::2])]

print(solution([50, 60, 60, 45, 70]))