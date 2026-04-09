# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        resHead = None
        curResNode = None

        while list1 or list2:
            
            while list1 and (not list2 or list1.val <= list2.val):
                if resHead is None:
                    resHead = list1
                    curResNode = resHead
                else:
                    curResNode.next=list1
                    curResNode = curResNode.next

                list1 = list1.next
                # curResNode.next.next = None

            while list2 and (not list1 or  list2.val < list1.val):
                if resHead is None:
                    resHead = list2
                    curResNode = resHead
                else:
                    curResNode.next=list2
                    curResNode = curResNode.next

                list2 = list2.next
                # curResNode.next.next = None

        return resHead
