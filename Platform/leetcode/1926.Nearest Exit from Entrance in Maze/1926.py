from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
      rows, cols = len(maze), len(maze[0])
      directions = [(0,1), (0,-1), (1,0), (-1,0)]
      q = deque([(entrance[0], entrance[1], 0)])
      
      maze[entrance[0]][entrance[1]] = '+'
      
      while q:
        r, c, steps = q.popleft()
        
        for dr, dc in directions:
          nr, nc = r + dr, c + dc
          if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
            if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
              return steps + 1
            
            maze[nr][nc] = '+'
            q.append((nr, nc, steps + 1))
            
      return -1
        
    
    
s = Solution()
print(s.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]))