class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        using dp 
        """
        res = curr = nums[0]

        for num in nums[1:]:
            curr = max(curr, 0) + num
            res = max(curr, res)

        return res