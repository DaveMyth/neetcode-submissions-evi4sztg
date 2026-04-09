# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        nextHead = dummy

        while tail:
            ctr = 0
            while tail and ctr < k:
                tail = tail.next
                ctr += 1

            tmp = None
            if tail:
                tmp = tail.next
                tail.next = None
            
                newHead, finalNode = self.reverseHelper(nextHead.next)
                nextHead.next = newHead
                nextHead = finalNode
                if (nextHead):
                    nextHead.next = tmp
                tail = nextHead


        return dummy.next

    def reverseHelper(self, head: Optional[ListNode]) -> list[ListNode]:

        if(not head or not head.next):
            return [head, head]

        newHead, finalNode = self.reverseHelper(head.next)
        if finalNode:
            finalNode.next = head
            finalNode = finalNode.next
            finalNode.next = None
            
        return [newHead, finalNode]