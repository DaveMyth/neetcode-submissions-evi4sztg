# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        res = None
        curResNode = None

        while l1 or l2:
            dig1 = l1.val if l1 else 0
            dig2 = l2.val if l2 else 0

            sumDig = (dig1 + dig2 + carry) % 10
            carry = (dig1 + dig2 + carry) // 10

            curSumNode = ListNode(sumDig)
            
            if not res:
                res = curSumNode
                curResNode = res
            else:
                curResNode.next = curSumNode
                curResNode = curResNode.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            curResNode.next = ListNode(carry)
        return res