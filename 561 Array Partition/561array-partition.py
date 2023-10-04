class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxsum=0
        n = len(nums)

        if n==2:
            return nums[0]
        for i in range(n):
            if i%2==0:
                maxsum += nums[i]
        return maxsum

        