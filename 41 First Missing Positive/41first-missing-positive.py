class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #swap elements/rearrangement
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] < n and nums[i] != nums[nums[i] - 1]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        #find missing
        for i in range(n):
            #since everything is sorted, check if its increasing and return first missing
            if nums[i] != i+1:
                return i+1

        return n + 1

        """
        s/c = O(1), in place array upgrade
        t/c = O(2n) = O(n)
        """
