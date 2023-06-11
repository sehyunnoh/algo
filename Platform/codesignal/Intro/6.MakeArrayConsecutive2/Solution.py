def solution(s):
  s.sort()
  return s[-1] - s[0] - len(s) + 1


def solution(statues):
    return max(statues) - min(statues) - len(statues) + 1