# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        
        def heightValidator(root: Optional[TreeNode]) -> int:

            if not root:
                return 0

            lH = heightValidator(root.left)
            rH = heightValidator(root.right)

            self.isBalanced = self.isBalanced and (abs(lH - rH) <= 1)

            return 1 + max(lH, rH)

        heightValidator(root)
        return self.isBalanced