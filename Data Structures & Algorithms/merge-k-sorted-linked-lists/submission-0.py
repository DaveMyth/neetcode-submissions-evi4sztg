# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:

            mergedLists = []

            for ctr in range(0, len(lists), 2):
                l1 = lists[ctr]
                l2 = lists[ctr + 1] if ctr + 1 < len(lists) else None
                mergedLists.append(self.mergedLists(l1, l2))

            lists = mergedLists
        return lists[0]
    
    def mergedLists(self, l1, l2):

        dummy = ListNode()
        tail = dummy

        while l1 or l2:
            
            if l1 and (not l2 or l1.val < l2.val):
                tail.next = l1
                l1 = l1.next
            elif l2:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        return dummy.next