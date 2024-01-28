from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
  def __str__(self):
    result = ''
    while self is not None:
      result += str(self.val)
      if self.next:
        result += " -> "
      self = self.next
    return result
      
      
    
class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    newNode = ListNode(-101)
    tail = newNode
    while head:
      tempNode = ListNode(head.val)
      if tail.val != tempNode.val:
        tail.next = tempNode
        tail = tail.next
      head = head.next
    return newNode.next

l32 = ListNode(3)
l31 = ListNode(3, l32)
l21 = ListNode(2, l31)
l12 = ListNode(1, l21)
l11 = ListNode(1, l12)

s = Solution()
print(s.deleteDuplicates(l11))


