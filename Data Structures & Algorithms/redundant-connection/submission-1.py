class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        N = len(edges)
        parent = [ctr for ctr in range(N+1)] #because there can be N+1 nodes
        rank = [1] * (N+1)

        def find(n1: int) -> int:
            if parent[n1] != n1:
                parent[n1] = find(parent[n1])
            return parent[n1]

        def union(n1: int, n2:int) -> bool:
            n1p, n2p = find(n1), find(n2)

            if n1p == n2p:
                return False

            if rank[n1p] > rank[n2p]:
                parent[n2p] = n1p
                rank[n1p] += 1
            else:
                parent[n1p] = n2p
                rank[n2p] += 1
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1,n2]
        