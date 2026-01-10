class Trie:
    def __init__(self):
        self.children = [None]*26
        self.end = False

    def insert(self, word):
        node = self

        for c in word:
            #find index to insert
            idx = ord(c) - ord('a')

            if node.children[idx] is None:
                #create an instance of the character in the trie
                node.children[idx] = Trie()

            #move to the word/chsrscter
            node = node.children[idx]

        #update flag
        node.end = True

    def search(self, word):
        node = self

        for c in word:

            idx = ord(c) - ord('a')

            if node.children[idx] is None:
                return False

            node = node.children[idx]

        return node.end

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(word):

            if not word:
                return [[]]

            res = []

            for i in range(1, len(word)+1):
                prefix = word[:i]

                #search for prefix in trie
                if trie.search(prefix):
                    #recursively search for the rest of the word
                    suffix = dfs(word[i:])

                    for w in suffix:
                        res.append([prefix]+w)

            return res

        trie = Trie()

        #add elements to trie
        for word in wordDict:
            trie.insert(word)

        #find all combinations
        permutations = dfs(s)

        return [' '.join(combo) for combo in permutations]