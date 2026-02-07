class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        No b should appear after an a

        s/c = O(n+1)
        t/c = O(n)
        """
        n, bCount = len(s), 0
        dp = [0] * (n + 1)   

        for i, char in enumerate(s, 1):
            if char == 'b':
                #no deletion
                dp[i] = dp[i-1]
                bCount += 1

            else:
                #delete/ keep track of the a and find mean deletions
                dp[i] = min(dp[i-1] + 1 , bCount)


        return dp[n]
