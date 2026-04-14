class TrieNode:

    def __init__(self):
        self.children = {}
        self.leaf = False

class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.trie

        ctr = 0
        while ctr < len(word) and word[ctr] in curr.children:
            curr = curr.children[word[ctr]]
            ctr += 1

        if ctr == len(word):
            curr.leaf = True
            return

        while ctr < len(word):
            curr.children[word[ctr]] = TrieNode()
            curr = curr.children[word[ctr]]
            ctr += 1
        curr.leaf = True

    def search(self, word: str) -> bool:
        ctr = 0
        curr = self.trie
        while ctr < len(word) and word[ctr] in curr.children:
            curr = curr.children[word[ctr]]
            ctr += 1

        return ctr == len(word) and curr.leaf

    def startsWith(self, prefix: str) -> bool:
        ctr = 0
        curr = self.trie
        while ctr < len(prefix) and prefix[ctr] in curr.children:
            curr = curr.children[prefix[ctr]]
            ctr += 1

        return ctr == len(prefix)
        