"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodeHash = {}
        resHead = None
        curResNode = None
        curNode = head

        while curNode:
            curNewNode = Node(curNode.val)
            if resHead is None:
                resHead = curNewNode
                curResNode = curNewNode
            else:
                curResNode.next = curNewNode
                curResNode = curResNode.next

            nodeHash[curNode] = curResNode
            curNode = curNode.next

        curNode = head
        curResNode = resHead

        while curNode:
            if curNode.random:
                curResNode.random = nodeHash[curNode.random]

            curNode = curNode.next
            curResNode = curResNode.next
        
        return resHead