from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # numCount = Counter(nums)

        # for key, val in numCount.items():
        #     if val == 1:
        #         return key
        #length of nums is 1 return nums[0]
        #missing =0
        missing=(2*(sum(set(nums))))-sum(nums)
        return missing