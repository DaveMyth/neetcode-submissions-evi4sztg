class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()

            node = node.children[c]
        node.isLeaf = True
                
    def search(self, word: str) -> bool:
        
        def dfs(currIdx: int, currNode: "TrieNode") -> bool:

            if currIdx == len(word):
                return currNode.isLeaf

            if word[currIdx] != '.' and word[currIdx] in currNode.children:
                return dfs(currIdx + 1, currNode.children[word[currIdx]]) 

            if word[currIdx] == '.':
                for c in currNode.children.keys():
                    if dfs(currIdx + 1, currNode.children[c]):
                        return True
            return False

        return dfs(0, self.root)
            
