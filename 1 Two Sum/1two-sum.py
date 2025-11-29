class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumKeeper = {}
        for i, num in enumerate(nums):
            diff = target - num

            if diff in sumKeeper:
                return [sumKeeper[diff], i]

            else:
                sumKeeper[num] = i

        
            