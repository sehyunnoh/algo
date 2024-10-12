from typing import List

class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    i = 0
    result = []
    while i < len(asteroids):
      v = asteroids[i]
      if result:
        c = result[-1]
        if c > 0 and v < 0:
          diff = c + v
          if diff == 0:
            result.pop()
            i += 1
            continue
          elif diff > 0:
            i += 1
            continue
          else:
            result.pop()
            continue
        else:
          result.append(v)
          i += 1
      else:
        result.append(v)
        i += 1
    return result
  
s = Solution()
print(s.asteroidCollision([5,10,-5]))
print(s.asteroidCollision([8,-8]))
print(s.asteroidCollision([10,2,-5]))
print(s.asteroidCollision([-2,-1,1,2]))
print(s.asteroidCollision([-2,-2,1,-2]))
print(s.asteroidCollision([-2,1,-2,-1]))