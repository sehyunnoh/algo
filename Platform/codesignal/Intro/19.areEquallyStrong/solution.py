def solution(yl, yr, fl, fr):
  return max(yl, yr) == max(fl, fr) and (yl+yr) == (fl+fr)

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return sorted([yourLeft,yourRight])==sorted([friendsLeft,friendsRight])

print(solution(10,15,15,10))