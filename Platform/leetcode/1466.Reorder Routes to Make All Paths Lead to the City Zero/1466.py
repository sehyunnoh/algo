from typing import List

class Solution:
  def minReorder(self, n: int, connections: List[List[int]]) -> int:
    edges = { (a,b) for a,b in connections}
    neighbors = { city: [] for city in range(n)}
    visit = set()
    changes = 0
    
    for a, b in connections:
      neighbors[a].append(b)
      neighbors[b].append(a)
      
    def dfs(city):
      nonlocal edges, neighbors, visit, changes
      
      for neighbor in neighbors[city]:
        if neighbor in visit:
          continue
        if (neighbor, city) not in edges:
          changes += 1
        visit.add(neighbor)
        dfs(neighbor)
    visit.add(0)
    dfs(0)
    return changes
  
s = Solution()
print(s.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))