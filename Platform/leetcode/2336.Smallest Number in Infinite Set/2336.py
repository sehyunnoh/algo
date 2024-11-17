class SmallestInfiniteSet:
    def __init__(self):
        self.s = set()
        return None
    def popSmallest(self) -> int:
        i = 1
        while True:
          if i not in self.s:
              self.s.add(i)
              return i
          else:
              i += 1
    def addBack(self, num: int) -> None:
        if num in self.s:
            self.s.remove(num)
        return None 