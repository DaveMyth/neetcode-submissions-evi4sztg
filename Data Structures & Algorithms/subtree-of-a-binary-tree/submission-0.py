# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def preOrder(root: Optional[TreeNode]) -> list:

            currList = []
            if not root:
                return currList

            if root.left:
                currList.extend(preOrder(root.left))
            else:
                currList.append("None")

            if root.right:
                currList.extend(preOrder(root.right))
            else:
                currList.append("None")

            currList.append(str(root.val))

            return currList

        l1 = "".join(preOrder(root))
        l2 = "".join(preOrder(subRoot))

        return l2 in l1

        

        

