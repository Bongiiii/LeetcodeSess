class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.endFlag = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:

            indx = ord(c) - ord('a')

            if curr.children[indx] is None:
                curr.children[indx] = TrieNode()

            curr = curr.children[indx]

        curr.endFlag = True

    def search(self, word: str) -> bool:
        #search helper
        def searchHelper(word_sub, node):
            for i in range(len(word_sub)):
                char = word_sub[i]

                if char == '.':
                    for child_node in node.children:
                        if child_node:
                            if searchHelper(word_sub[i+1:], child_node):
                                return True

                    return False  

                else:    
                    indx = ord(char) - ord('a')  
                    if node.children[indx] is None:
                        return False
                    node = node.children[indx]

            return node.endFlag 

        return searchHelper(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)