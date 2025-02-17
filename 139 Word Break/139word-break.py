class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Using memoization and backtracking
        we use memoization to avoid redudancy

        s/c = O(N), memoization array
        t/c O(N^2 * m), m = len of wordDict, n size of s

        """
        memo: Dict[int, bool] = {}

        def helper(startIdx):
            #base case
            if startIdx == len(s):
                return True

            if startIdx in memo:
                return memo[startIdx]

            #flag to check for startidx
            ans = False

            for word in wordDict:
                if s[startIdx:].startswith(word):
                    if helper(startIdx + len(word)):
                        ans =  True
                        break

            memo[startIdx] = ans
            return ans
        
        return helper(0)