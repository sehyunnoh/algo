from typing import List

class Solution:
  def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    visited = set({0})
    stack = rooms[0]
    
    while stack:
      current_room = stack.pop()
      visited.add(current_room)
      for key in rooms[current_room]:
        if key not in visited:
          stack.append(key)
    
    return len(rooms)  == len(visited)
      
  
s = Solution()
print(s.canVisitAllRooms([[1],[2],[3],[]]))
print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))