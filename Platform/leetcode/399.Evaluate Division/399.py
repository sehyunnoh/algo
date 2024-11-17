from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for (A, B), value in zip(equations, values):
            graph[A].append((B, value))       # A → B with weight value
            graph[B].append((A, 1 / value))  # B → A with weight 1 / value
        
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            
            queue = deque([(start, 1.0)])  # (current_node, current_product)
            visited = set()
            
            while queue:
                current, product = queue.popleft()
                if current == end:
                    return product
                
                visited.add(current)
                
                for neighbor, value in graph[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, product * value))
            
            return -1.0  # No path found
        return [bfs(x, y) for x, y in queries]