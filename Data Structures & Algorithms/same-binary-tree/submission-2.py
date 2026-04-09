# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.l1 = []
        self.l2 = []
        
        def dfs(root, l):

            if not root:
                return

            if root.left:
                dfs(root.left, l)
            else:
                l.append(None)

            if root.right:
                dfs(root.right, l)

            else:
                l.append(None)

            l.append(root.val)

            return

        dfs(p, self.l1)
        dfs(q, self.l2)

        print(self.l1, self.l2)

        if len(self.l1) != len(self.l2):
            return False
        
        for ctr in range (len(self.l1)):
            if self.l1[ctr] != self.l2[ctr]:
                return False

        return True