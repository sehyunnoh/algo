from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = cur = ListNode(next=head)
        while head:
            if head.val != val:
                cur.next =  head
                cur = cur.next
            head = head.next
        cur.next = None
        return dummy.next
      

      
      
six_2 = ListNode(val=6)
five = ListNode(5, six_2)
four = ListNode(4, five)
three = ListNode(3, four)
six = ListNode(6,three)
two = ListNode(2, six)
one = ListNode(1, two)

s = Solution()
s.removeElements(one, 6)