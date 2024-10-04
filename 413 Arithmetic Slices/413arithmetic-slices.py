class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
         # If nums has less than 3 elements, there can't be any arithmetic subarrays
        if len(nums) < 3:
            return 0
        
        total_slices = 0
        current_slices = 0
        
        # Traverse through the array starting from the second index
        for i in range(2, len(nums)):
            # Check if the current subarray (nums[i-2], nums[i-1], nums[i]) forms an arithmetic slice
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                # If it does, increment the current_slices counter
                current_slices += 1
                # Add the number of current slices to the total
                total_slices += current_slices
            else:
                # Reset the current_slices counter if the slice breaks
                current_slices = 0
        
        return total_slices