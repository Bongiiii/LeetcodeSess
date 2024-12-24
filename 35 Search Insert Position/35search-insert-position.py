class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        
        """
        # #first check if target in array number
        # if target in nums:
        #     return nums.index(target)
        #  #if not there
        # else:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2  # Calculate the middle index
            
            if nums[mid] == target:  # Target found
                return mid
            elif nums[mid] < target:  # Target lies to the right
                low = mid + 1
            else:  # Target lies to the left
                high = mid - 1
        
        # If target is not found, `low` will be the insertion index
        return low