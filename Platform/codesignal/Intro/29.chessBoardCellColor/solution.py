def solution(c1, c2):
  return (ord(c2[0]) - ord(c1[0])) % 2 == (int(c2[1]) - int(c1[1])) % 2



# print(solution("A1", "C3"))
print(solution("A1", "B2"))