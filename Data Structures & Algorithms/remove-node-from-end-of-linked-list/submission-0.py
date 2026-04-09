# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        lenCtr = 0
        curNode = head

        while curNode:
            lenCtr += 1
            curNode = curNode.next

        if n == lenCtr:
            if head:
                head = head.next
                return head
            return None

        removeNodeIdx = lenCtr - n #to get to the node before the node to be removed
        idxMonitor = 1
        curNode = head

        while curNode and idxMonitor < removeNodeIdx:
            curNode = curNode.next
            idxMonitor += 1

        if curNode and curNode.next:
            curNode.next = curNode.next.next

        return head