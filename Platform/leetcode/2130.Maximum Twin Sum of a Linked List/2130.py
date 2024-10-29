from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
      cur, arr, result = head, [], 0
      while cur:
        arr.append(cur.val)
        cur = cur.next
      for i in range(len(arr)//2):
        result = max(result, (arr[i] + arr[-i-1]))
      return result
      
        
      
    
s = Solution()

one = ListNode(1, None)
two = ListNode(2, one)
four = ListNode(4, two)
five = ListNode(5, four)

print(s.pairSum(five))