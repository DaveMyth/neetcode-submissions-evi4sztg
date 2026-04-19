class TrieNode:

    def __init__(self):
        self.children = {}
        self.isLeaf = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        #Create a trie of words
        root = TrieNode()

        for word in words:
            currNode = root
            for c in word:
                if c not in currNode.children:
                    currNode.children[c] = TrieNode()
                currNode = currNode.children[c]

            currNode.isLeaf = True

        #Perform DFS
        visited = [[False for ctr in range(len(board[0]))] for ctr2 in range(len(board))]
        res = set()

        def dfs(i: int, j: int, currNode: "TrieNode", currWord: str) -> None:

            if currNode.isLeaf and currWord not in res:
                res.add(currWord)

            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or visited[i][j] or board[i][j] not in currNode.children:
                return

            visited[i][j] = True
            dfs(i-1, j, currNode.children[board[i][j]], currWord+board[i][j])
            dfs(i+1, j, currNode.children[board[i][j]], currWord+board[i][j])
            dfs(i, j-1, currNode.children[board[i][j]], currWord+board[i][j])
            dfs(i, j+1, currNode.children[board[i][j]], currWord+board[i][j])
            visited[i][j] = False

        for ctr1 in range(len(board)):
            for ctr2 in range(len(board[0])):
                if board[ctr1][ctr2] in root.children:
                    dfs(ctr1, ctr2, root, "")

        return list(res)