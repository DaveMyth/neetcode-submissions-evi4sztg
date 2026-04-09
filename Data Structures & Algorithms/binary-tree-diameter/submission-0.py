# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0
        
        def diameterHelper( root: Optional[TreeNode]) -> int:

            if not root:
                return 0

            leftH = diameterHelper(root.left)
            rightH = diameterHelper(root.right)

            currDiameter = leftH + rightH
            self.diameter = max(self.diameter, currDiameter)

            return 1 + max(leftH, rightH)

        diameterHelper(root)
        return self.diameter