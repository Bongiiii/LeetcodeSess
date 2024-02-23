class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_sqr = []
        for i in range(len(nums)):
            sqr = (nums[i])**2
            sorted_sqr.append(sqr)

        sorted_sqr.sort()
        return sorted_sqr
