# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        nodeQueue = [[root]]

        if not root:
            return []
        
        while nodeQueue:
            curLvl = nodeQueue.pop()
            nextLevel = []
            curRes = []

            for node in curLvl:
                curRes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)

                if node.right:
                    nextLevel.append(node.right)
            res.append(curRes)
            if nextLevel:
                nodeQueue.append(nextLevel)
        return res