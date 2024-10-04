class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        Understand:
        input - unsorted array, output - integer
        problem summary: given an unsorted array, return the length of the longest continuos subarray
        
        Match:
        array manipulation
        pointers
        sliding window
        
        Plan:
        initialize two variables to stoore the max length seen so far and current length of window/subarray
        iterate whole array checking if consecutive elements are strictly increasing
        if so continue counting length of subarray
        when they break the strictly increasing streak, reset current length to one and update maxlength if necessary
        return maxlength between maxlength and currlength
        
        R/E:
        s/c = O(1), t/c = O(N)
        """
        length, currLength = 1, 1
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                currLength += 1
            else:
                length = max(length, currLength)
                currLength = 1
            
        return max(length, currLength)