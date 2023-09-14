def solution(inputArray, elemToReplace, substitutionElem):
  return [substitutionElem if x == elemToReplace else x for x in inputArray ]


print(solution([1,2,1], 1, 3))