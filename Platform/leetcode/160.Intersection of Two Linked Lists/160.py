from typing import Optional

class ListNode:
  def __init__(self, x, next=None):
    self.val = x
    self.next = next
    

class Solution:
  # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
  #     l1, l2 = headA, headB
  #     while l1 != l2:
  #       l1 = l1.next if l1 else headB
  #       l2 = l2.next if l2 else headA
  #     return l1
    
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
      s = set()
      while headA:
        s.add(headA)
        headA = headA.next
      while headB:
        if headB in s:
          return headB
        headB = headB.next
      return None

c5 = ListNode(5)
c4 = ListNode(4, c5)
c8 = ListNode(8, c4)
a1 = ListNode(1, c8)
a4 = ListNode(4, a1)
b1 = ListNode(1, c8)
b6 = ListNode(6, b1)
b5 = ListNode(5, b6)

s = Solution()
print(s.getIntersectionNode(a4, b5))
  

