# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                fast = None

        reverseHead, finalNode = self.reverseList(slow.next)
        slow.next = None
        
        forward = head
        backward = reverseHead
        curNode = None

        while forward or backward:
            if curNode is None and forward:
                curNode = forward
                forward = forward.next if forward else None
            
            elif forward:
                curNode.next = forward
                curNode = curNode.next
                forward = forward.next if forward else None
            
            if backward:
                curNode.next = backward
                curNode = curNode.next
                backward = backward.next if backward else None


    
    def reverseList(self, head: Optional[ListNode]) -> list[ListNode]:

        if not head or not head.next:
            return [head, head]
        
        newHead, curNewNode = self.reverseList(head.next)
        curNewNode.next = head
        curNewNode = curNewNode.next
        curNewNode.next = None

        return [newHead, curNewNode]