# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
      res = ''
      while self.next is not None:
        res += str(self.val) + " -> "
        self = self.next
      res += str(self.val)
      return res
        

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      head = cur = ListNode()
      while True:
        if list1 == None and list2 == None:
          break
        elif list1 == None and list2 != None:
          cur.next = list2
          cur, list2 = cur.next, list2.next
        elif list1 != None and list2 == None:
          cur.next = list1
          cur, list1 = cur.next, list1.next
        else:
          if list1.val > list2.val:
            cur.next = list2
            cur, list2 = cur.next, list2.next
          else:
            cur.next = list1
            cur, list1 = cur.next, list1.next
      return head.next
        
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         head = cur = ListNode()
#         while list1 and list2:               
#             if list1.val < list2.val:
#                 cur.next = list1
#                 list1, cur = list1.next, list1
#             else:
#                 cur.next = list2
#                 list2, cur = list2.next, list2
                
#         if list1 or list2:
#             cur.next = list1 if list1 else list2
            
#         return head.next    
    
l14 = ListNode(4)
l12 = ListNode(2, l14)
l11 = ListNode(1, l12)
# print(l11)

l24 = ListNode(4)
l23 = ListNode(3, l24)
l21 = ListNode(1, l23)
# print(l21)

s = Solution()
print(s.mergeTwoLists(l11, l21))