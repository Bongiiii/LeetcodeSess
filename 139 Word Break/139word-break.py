class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        U:
        check if word can be segmented according to wordDict 
        input - string and list of strings , output - boolean

        M:
        dp
        memoization
        string manipulation

        P:
        put dictionary into a set as to remove duplicates
        then have a dp array of the size if the input string, which keeps
         booleans that determine if that segment is in wordset
        an empty can always be segmented 
        return if the entire string can be segmented

        I:

        R/E:
        s/c = O(n + m.k), n - size of dp array, m -  word dict, k - average length of word
        t/c = O(n^3), 

        """
        wordSet = set(wordDict)

        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            dp[i] = any( dp[j] and s[j:i] in wordSet for j in range(i))

        return dp[len(s)]