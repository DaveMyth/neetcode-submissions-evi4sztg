# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxSum = float("-inf")

        def maxPathSumHelper(root: Optional[TreeNode]) -> int:

            if not root:
                return 0

            lMaxSum = maxPathSumHelper(root.left)
            rMaxSum = maxPathSumHelper(root.right)

            self.maxSum = max(root.val, lMaxSum + root.val, rMaxSum + root.val, lMaxSum + rMaxSum + root.val, self.maxSum)
            return max(max(lMaxSum, rMaxSum) + root.val, root.val)

        maxPathSumHelper(root)
        return self.maxSum