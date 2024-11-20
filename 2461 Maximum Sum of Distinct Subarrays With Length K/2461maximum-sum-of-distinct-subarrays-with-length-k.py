class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        Understand:
        input - array, integer; output - integer
        Edgecase - can the subarray window be more than the array length say, array length is 2 and k = 3

        Match:
        sliding window
        array manipulation

        Plan:
        initialize a variable that keeps track of the window sum and another to track max subarray 
         max which will be using to keep the max sum seen in the subarray so far
        initialize the start of the window and end as a tuple
        iterate the array once
        have a set to keep track of duplicates, and when numbers repeat, update window
        
        R/E:
        s/c = O(1)
        t/c = O(N)
        """
        if len(nums) < k:
            return 0
        
        winSum, maxSubSum = 0, 0
        intSet = {}
        start = 0

        for end in range(len(nums)):
            # Add current element to window
            winSum += nums[end]
            intSet[nums[end]] = intSet.get(nums[end], 0) + 1
            
            # If window size becomes k
            if end - start + 1 == k:
                # If all elements are unique
                if len(intSet) == k:
                    maxSubSum = max(maxSubSum, winSum)
                
                # Remove the leftmost element
                winSum -= nums[start]
                intSet[nums[start]] -= 1
                if intSet[nums[start]] == 0:
                    del intSet[nums[start]]
                start += 1
                
        return maxSubSum