# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.numList = []

        def inOrderTraversal(root: Optional[TreeNode]) -> None:

            if root.left:
                inOrderTraversal(root.left)

            self.numList.append(root.val)

            if root.right:
                inOrderTraversal(root.right)

        inOrderTraversal(root)

        return self.numList[k-1]