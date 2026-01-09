class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, count = 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1

            if count > k:
                #maintain window size but reduce count
                if nums[left] == 0:
                    count -= 1

                #expand window for ones
                left += 1

        return len(nums) - left