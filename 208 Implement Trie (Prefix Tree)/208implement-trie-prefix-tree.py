class Trie:

    def __init__(self):
        self.childNodes = [None] * 26
        self.endOfword = False

    def insert(self, word: str) -> None:
        currNode = self

        for c in word:
            indexPos = ord(c) - ord('a')

            if currNode.childNodes[indexPos] is None:
                currNode.childNodes[indexPos] = Trie()

            currNode = currNode.childNodes[indexPos]

        currNode.endOfword = True

    #search helper
    def searchHelper(self, word):
        currNode = self

        for c in word:
            indexPos = ord(c) - ord('a')

            if currNode.childNodes[indexPos] is None:
                return None

            currNode = currNode.childNodes[indexPos]

        return currNode

    def search(self, word: str) -> bool:
        searchNodes = self.searchHelper(word)

        return searchNodes is not None and searchNodes.endOfword

    def startsWith(self, prefix: str) -> bool:
        searchPrefix = self.searchHelper(prefix)

        return searchPrefix is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)