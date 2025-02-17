class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Understand:
        input - array of integers, output - boolean
        what if you have one element?

        Match:
        math
        array manipulation
        two pointers/ sliding window
        dynamic programming

        Plan: 
       using parity, if odd then can't be made into 2 equal subsets

        R/E:(bruteforce)
        s/c = O(target)
        t/c = O(n*target)
        """
        total = sum(nums)
        # If total is odd, we cannot partition it into two equal subsets
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # Initialize a DP array where dp[i] is True if subset sum i is achievable
        dp = [False] * (target + 1)
        dp[0] = True  # Zero sum is always possible (by choosing no elements)
        
        # Process each number in the array
        for num in nums:
            # Iterate backwards to avoid using the same number more than once
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]