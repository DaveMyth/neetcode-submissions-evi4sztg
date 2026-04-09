# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        nodeQ = [[root]]
        res = [root.val]

        while nodeQ:
            curLvl = nodeQ.pop()
            nxtLvl = []
            
            for node in curLvl:
                
                if node.left:
                    nxtLvl.append(node.left)

                if node.right:
                    nxtLvl.append(node.right)

            if nxtLvl:
                nodeQ.append(nxtLvl)
                res.append(nxtLvl[-1].val)
        return res