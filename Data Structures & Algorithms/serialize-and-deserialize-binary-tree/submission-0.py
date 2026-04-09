# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        def preorder(root: Optional[TreeNode]) -> list[str]:

            if not root:
                return ["None"]

            leftList = preorder(root.left)
            rightList = preorder(root.right)

            leftList.insert(0,str(root.val))
            leftList.extend(rightList)

            return leftList

        compList = preorder(root)
        serialized = ",".join(compList)

        return serialized
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        self.dataList = data.split(",")

        def deserializeHelper() -> Optional[TreeNode]:

            nodeVal = self.dataList.pop(0)
            if nodeVal == "None":
                return None

            leftTree = deserializeHelper()
            rightTree = deserializeHelper()

            curNode = TreeNode(int(nodeVal))
            curNode.left = leftTree
            curNode.right = rightTree
            return curNode

        root = deserializeHelper()
        return root