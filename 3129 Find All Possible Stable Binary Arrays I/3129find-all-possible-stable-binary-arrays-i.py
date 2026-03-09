class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(i, j, k):
            # Base Case: No more zeros left
            if i == 0:
                # If we are placing ones (k=1), and the remaining ones 
                # fit within the limit, it's a valid path.
                return 1 if (k == 1 and j <= limit) else 0
            
            # Base Case: No more ones left
            if j == 0:
                return 1 if (k == 0 and i <= limit) else 0

            # Logic for placing a 0 (k=0) or a 1 (k=1)
            if k == 0:
                # This is where you'd implement your transition logic
                # For example, a simple version (without the limit subtraction logic):
                res = dfs(i - 1, j, 0) + dfs(i - 1, j, 1)
                # If i > limit, you'd subtract the invalid cases here
                if i > limit:
                    res -= dfs(i - limit - 1, j, 1)
            else:
                res = dfs(i, j - 1, 0) + dfs(i, j - 1, 1)
                if j > limit:
                    res -= dfs(i, j - limit - 1, 0)
            
            return res % MOD

        # The result is the sum of starting with a 0 or starting with a 1
        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD