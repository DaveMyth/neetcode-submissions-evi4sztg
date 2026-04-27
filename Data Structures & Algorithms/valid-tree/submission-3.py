class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not edges:
            return True

        adjList = { node: [] for node in range(n) }

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)  

        visited = set()

        def dfs(curr: int, prev: int) -> bool:
            if curr in visited:
                return False
            
            visited.add(curr)
            for node in adjList[curr]:
                if node != prev:
                    if not dfs(node, curr):
                        return False
            return True
        
        for ctr in range(n):
            if not dfs(ctr, -1):
                return False
            if len(visited) == n:
                return True

        return False