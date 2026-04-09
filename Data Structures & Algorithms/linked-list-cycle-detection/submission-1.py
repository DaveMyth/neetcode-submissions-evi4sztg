# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        oneHop = twoHop = head

        while twoHop:
            oneHop = oneHop.next
            twoHop = twoHop.next
            if(not twoHop):
                return False
            twoHop = twoHop.next

            if(oneHop and twoHop and oneHop.val == twoHop.val):
                return True
        return False