from typing import List

class Solution:
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = [False] * n
    
    def dfs(city):
      for neighbor in range(n):
        if isConnected[city][neighbor] == 1 and not visited[neighbor]:
          visited[neighbor] = True
          dfs(neighbor)
    
    provinces = 0
    for city in range(n):
      if not visited[city]:
        dfs(city)
        provinces += 1
    return provinces

  
s = Solution()
print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))