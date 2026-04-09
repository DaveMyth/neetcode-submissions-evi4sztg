# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodeCtr = 0

        def goodNodeHelper(root: TreeNode, maxNoFromRoot: float) -> None:

            if maxNoFromRoot <= root.val:
                self.goodNodeCtr += 1

            if root.left:
                goodNodeHelper(root.left, max(maxNoFromRoot, root.val))

            if root.right:
                goodNodeHelper(root.right, max(maxNoFromRoot, root.val))

        goodNodeHelper(root, float("-inf"))

        return self.goodNodeCtr