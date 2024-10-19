# Time limit exceeded
# class RecentCounter:

#     def __init__(self):
#         self.q = []

#     def ping(self, t: int) -> int:
#         self.q.append(t)
#         return len([x for x in self.q if t-3000 <= x <= t])
      
class RecentCounter:

    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.pop(0)
        return len(self.q)
  
  
obj = RecentCounter()
param_1 = obj.ping(t)