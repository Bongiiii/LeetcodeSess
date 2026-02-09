class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # p, q, i = 0, 0, 0

        # while i < len(nums):
        #     if nums[i] < nums[i+1]:
        #         i += 1

        # p = nums[i]

        # while i < len(nums):
        #     if nums[i] > nums[i+1]:
        #         i += 1

        # q = nums[i]

        # if p == q:
        #     return i

        i, j, peak = 0, len(nums) - 1, -1

        while (i <= j):
            mid = (i+j) // 2

            if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
                peak = mid
                j = mid - 1

            else:
                i = mid + 1

        return peak