class Trie:

    def __init__(self):
       #initialize a dicttionary to store trie nodes
       self.root = {} 

    def insert(self, word: str) -> None:
        #first create a node
        node = self.root

        #iterate through the words 
        for char in word:
            #first check if word is already inserted
            if char not in node:
                #create an instance of it
                node[char] = {}

            node = node[char]

        #maker/ flagger to make end of word
        node["#"] = True

    def search(self, word: str) -> bool:
        #first create a node
        node = self.root

        #iterate through word
        for char in word:
            if char not in node:
                return False

            node = node[char]

        #maker for when at the end of the word
        return "#" in node
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root

        #iterate in prefixes
        for char in prefix:
            if char not in node:
                return False

            node = node[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)