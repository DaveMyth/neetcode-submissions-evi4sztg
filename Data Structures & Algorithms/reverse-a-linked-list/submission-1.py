# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        if not head.next:
            return head

        newHead = self.reverseList(head.next)
        node = newHead
        while(node.next):
            node = node.next

        node.next = head
        head.next = None
        return newHead