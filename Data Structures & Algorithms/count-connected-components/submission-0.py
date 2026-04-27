class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if n <= 1:
            return n

        adjList = {node: [] for node in range(n) }
        visited = set()
        connSetsCtr = 0

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(curr: int) -> None:
            if curr in visited:
                return
            
            visited.add(curr)
            for nb in adjList[curr]:
                dfs(nb)
        
        currNode = 0
        while currNode < n:
            if currNode not in visited:
                connSetsCtr += 1
                dfs(currNode)

            currNode += 1

        return connSetsCtr