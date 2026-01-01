from itertools import pairwise

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.pos = -1

    def insert(self, word, index):
        curr = self

        for w in word:

            idx = ord(w) - ord('a')

            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]

        curr.pos = index

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols, output, directions = len(board), len(board[0]), [], (-1,0,1,0,-1)

        def dfs(node, row, col):
            index = ord(board[row][col]) - ord('a')
            
            if node.children[index] is None:
                return 

            node = node.children[index]

            if node.pos >= 0:
                output.append(words[node.pos])
                node.pos = -1

            temp = board[row][col]
            board[row][col] = "&"

            for a, b in pairwise(directions):
                new_row, new_col = a + row, b + col

                if (0<=new_row<rows) and (0<=new_col<cols) and board[new_row][new_col] != "&":
                    dfs(node, new_row, new_col)

            board[row][col] = temp

        trie = TrieNode()

        for i, w in enumerate(words):
            trie.insert(w, i)

        for i in range(rows):
            for j in range(cols):
                dfs(trie, i, j)

        return output

