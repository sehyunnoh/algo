# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#       if not head.next:
#         return None
#       slow = head
#       fast = head.next.next
      
#       while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
        
#       slow.next = slow.next.next
#       return head

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head.next:
        return None
      
      current = head
      i = 0
      while current:
        current = current.next
        i += 1
      half = i // 2

      current = head
      i = 0
      while current:
        if i == (half - 1):
            current.next = current.next.next
            break
        current = current.next
        i += 1
      return head
    
six = ListNode(6)
two = ListNode(2, six)
one = ListNode(1, two)
seven = ListNode(7, one)
four = ListNode(4, seven)
three = ListNode(3, four)
zero = ListNode(1, three)

s = Solution()
s.deleteMiddle(zero)


