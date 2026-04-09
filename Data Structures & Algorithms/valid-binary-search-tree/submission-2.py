# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.inOrder = []

        def inorderTraversal(root: TreeNode) -> None:

            if root.left:
                inorderTraversal(root.left)

            self.inOrder.append(root.val)
            
            if root.right:
                inorderTraversal(root.right)

        inorderTraversal(root)\

        for ctr in range (1, len(self.inOrder)):
            if self.inOrder[ctr - 1] >= self.inOrder[ctr]:
                return False

        return True