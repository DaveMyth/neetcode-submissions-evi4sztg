"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}

        def dfs(oldNode: "Node", newNode: "Node") -> None:

            newNode = Node(oldNode.val)
            nodeMap[oldNode.val] = newNode

            for neighbor in oldNode.neighbors:
                if neighbor.val not in nodeMap:
                    dfs(neighbor, None)

                newNode.neighbors.append(nodeMap[neighbor.val])

            return newNode

        if not node:
            return None

        dfs(node, None)
        return nodeMap[node.val]