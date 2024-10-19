class Solution:
  def predictPartyVictory(self, senate: str) -> str:
    r, d, n = [], [], len(senate)
    for i in range(n):
      if senate[i] == 'R':
        r.append(i)
      else:
        d.append(i)
    while r and d:
      rv, dv = r.pop(0), d.pop(0)
      if rv < dv:
        r.append(n)
      else:
        d.append(n)
      n += 1
    return 'Radiant' if r else 'Dire'

s = Solution()
print(s.predictPartyVictory("RD"))
print(s.predictPartyVictory("RDD"))
print(s.predictPartyVictory("D"))