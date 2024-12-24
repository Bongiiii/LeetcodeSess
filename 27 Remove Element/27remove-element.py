class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        just have a counter to count other number not val and when you get to the end of the array return couunt

        s/c = O(1), t/c=O(n)
        """
        left = 0  # Pointer to place the next valid element
    
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]  # Place the element at the left pointer
                left += 1  # Increment the left pointer

        return left  # The count of elements not equal to val
